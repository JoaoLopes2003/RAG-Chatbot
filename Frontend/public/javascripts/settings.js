export default class Settings {
    constructor() {

        // Basic Settings
        this.input_language_value = "English";
        this.input_language_el = document.getElementById('input_language');
        this.output_language_value = "English";
        this.output_language_el = document.getElementById('output_language');
        this.saveBasicSettings_el = document.getElementById('saveBasicSettings');
        this.basicSaveMsg_el = document.getElementById('basicSaveMsg');

        // Advanced Settings
        this.retrieve_only_chunks_value = false;
        this.retrieve_only_chunks_el = document.getElementById('retrieve_only_chunks');
        this.precise_chunking_value = false;
        this.precise_chunking_el = document.getElementById('precise_chunking');
        this.retrieve_limit_value = 10;
        this.retrieve_limit_el = document.getElementById('retrieve_limit');
        this.documents = {} // dict[str, list[str]], is a dictionary of folder names to lists of files names
        this.selectedDocuments = {};
        this.documents_container_el = document.getElementById('documents_container');
        this.saveAdvancedSettings_el = document.getElementById('saveAdvancedSettings');
        this.advancedSaveMsg_el = document.getElementById('advancedSaveMsg');
        this.spinner_el = document.getElementById('documentsSpinnerOverlay');
        this.openFolders = new Set();

        // Upload File
        this.uploadForm_el = document.getElementById('upload-file-container');
        this.templateFolder_el = document.getElementById('template_folder');
        this.newTemplateFolder_label = document.querySelector('label[for="new_template_folder"]');
        this.newTemplateFolder_input = document.getElementById('new_template_folder');
        this.fileInput_el = document.getElementById('loadfile');
        this.uploadButton_el = document.getElementById('upload_loadfilebutton');
        this.uploadFilename_el = document.getElementById('upload_filename');

        // Update File
        this.updateForm_el = document.getElementById('update-file-container');
        this.updateFolder_el = document.getElementById('update_folder');
        this.updateFileInput_el = document.getElementById('updated_file');
        this.updateFilename_el = document.getElementById('update_filename');
        this.updateButton_el = document.getElementById('update_loadfilebutton');

        this.initializeEventListeners();
        console.log("Settings instance created.");
    }

    // Converts the selectedDocuments object into the flat array
    getSourceFiles() {
        const sourceFiles = [];
        for (const folder in this.selectedDocuments) {
            for (const file of this.selectedDocuments[folder]) {
                sourceFiles.push(`${folder}/${file}`);
            }
        }
        return sourceFiles;
    }

    static async create() {
        const settingsInstance = new Settings();

        // Fetch the documents that exist in the server
        await settingsInstance.fetchDocuments();

        // Populate and initialize the upload form after fetching data
        settingsInstance.populateFolderDropdown();
        settingsInstance.populateUpdateFolderDropdown(); 

        settingsInstance.handleFolderSelectionChange();
        settingsInstance.renderDocuments();
        return settingsInstance;
    }

    populateUpdateFolderDropdown() {
        this.updateFolder_el.innerHTML = '';

        const folderNames = Object.keys(this.documents);
        if (folderNames.length === 0) {
            this.updateFolder_el.add(new Option("No folders available", "", true, true));
            this.updateFolder_el.disabled = true;
        } else {
            folderNames.forEach(folderName => {
                const option = new Option(folderName, folderName);
                this.updateFolder_el.add(option);
            });
            this.updateFolder_el.disabled = false;
        }
        console.log("Update folder dropdown populated.");
    }

    populateFolderDropdown() {
        this.templateFolder_el.innerHTML = '';

        // Add the "Default" option
        const defaultOption = new Option("undefined", "undefined");
        this.templateFolder_el.add(defaultOption);

        // Add options for each existing folder
        const folderNames = Object.keys(this.documents);
        folderNames.forEach(folderName => {
            const option = new Option(folderName, folderName);
            this.templateFolder_el.add(option);
        });

        // Add the "Create a new one" option at the end
        const createNewOption = new Option("Create a new one", "Create a new one");
        this.templateFolder_el.add(createNewOption);
        
        console.log("Template folder dropdown populated.");
    }

    async fetchDocuments() {
        console.log("Fetching documents from server...");
        try {
            const response = await fetch("http://localhost:3001/getallfiles");
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            this.documents = data.filenames;

            // By default, all documents are selected when first loaded.
            // We do a deep copy to avoid reference issues.
            this.selectedDocuments = JSON.parse(JSON.stringify(this.documents));
            
            console.log("Documents successfully loaded:", this.documents);
        } catch (error) {
            console.error("Failed to fetch documents:", error);
            this.documents = {};
            this.selectedDocuments = {};
        }
    }

    renderDocuments() {
        // Clear any existing content
        this.documents_container_el.innerHTML = '';

        if (Object.keys(this.documents).length === 0) {
            this.documents_container_el.textContent = 'No documents found.';
            return;
        }

        let folderIndex = 0;
        for (const folderName in this.documents) {
            folderIndex++;
            const files = this.documents[folderName];

            // Create the main .folder div
            const folderDiv = document.createElement('div');
            const isOpen = this.openFolders.has(folderName);
            folderDiv.className = isOpen ? 'folder open' : 'folder';
            folderDiv.dataset.folderName = folderName;

            // --- Create Folder Top Bar ---
            const folderTopDiv = document.createElement('div');
            folderTopDiv.className = 'folder-top';
            
            const arrow = document.createElement('div');
            arrow.className = 'arrow-left-folders';

            const folderCheckbox = document.createElement('input');
            folderCheckbox.type = 'checkbox';
            folderCheckbox.id = `folder${folderIndex}`;
            folderCheckbox.name = `folder${folderIndex}`;
            folderCheckbox.value = folderName;
            // A folder is checked if all its files are selected
            folderCheckbox.checked = this.selectedDocuments[folderName]?.length === files.length;
            
            const folderIcon = document.createElement('img');
            folderIcon.src = '/images/icon-folder.svg';
            folderIcon.alt = 'Folder Icon';

            const folderNameSpan = document.createElement('span');
            folderNameSpan.textContent = folderName;

            folderTopDiv.append(arrow, folderCheckbox, folderIcon, folderNameSpan);

            // --- Create Folder Files List ---
            const folderFilesDiv = document.createElement('div');
            folderFilesDiv.className = 'folder-files';

            let fileIndex = 0;
            files.forEach(fileName => {
                fileIndex++;
                const fileDiv = document.createElement('div');
                fileDiv.className = 'file';

                const fileCheckbox = document.createElement('input');
                fileCheckbox.type = 'checkbox';
                fileCheckbox.id = `file${folderIndex}-${fileIndex}`;
                fileCheckbox.name = `file${folderIndex}-${fileIndex}`;
                fileCheckbox.value = fileName;
                // Pass folder name via dataset for easier handling
                fileCheckbox.dataset.folder = folderName; 
                fileCheckbox.checked = this.selectedDocuments[folderName]?.includes(fileName);

                const fileInfoDiv = document.createElement('div');
                fileInfoDiv.className = 'file-info';

                const fileIcon = document.createElement('img');
                fileIcon.src = '/images/icon-file.svg';
                fileIcon.alt = 'File Icon';

                const fileLink = document.createElement('a');
                fileLink.href = `http://localhost:3001/getfile/${encodeURIComponent(`${folderName}/${fileName}`)}`;
                fileLink.textContent = fileName;
                
                const deleteIcon = document.createElement('img');
                deleteIcon.src = '/images/icon-delete-bin.svg';
                deleteIcon.alt = 'Delete Icon';
                deleteIcon.className = 'delete-icon'; // For targeting
                // Store file and folder info on the element for the event handler
                deleteIcon.dataset.file = fileName;
                deleteIcon.dataset.folder = folderName;

                fileInfoDiv.append(fileIcon, fileLink);
                fileDiv.append(fileCheckbox, fileInfoDiv, deleteIcon);
                folderFilesDiv.appendChild(fileDiv);
            });

            // Append everything to the main container
            folderDiv.append(folderTopDiv, folderFilesDiv);
            this.documents_container_el.appendChild(folderDiv);
        }
    }

    initializeEventListeners() {
        if (this.saveBasicSettings_el) {
            this.saveBasicSettings_el.addEventListener('click', (event) => {
                event.preventDefault();
                this.input_language_value = this.input_language_el.value;
                this.output_language_value = this.output_language_el.value;

                console.log("Basic settings saved!");
                this.basicSaveMsg_el.textContent = 'Saved!';
                this.basicSaveMsg_el.classList.add('visible');
                setTimeout(() => {
                    this.basicSaveMsg_el.classList.remove('visible');
                    this.basicSaveMsg_el.textContent = '';
                }, 2000);
            });
        }

        if (this.saveAdvancedSettings_el) {
            this.saveAdvancedSettings_el.addEventListener('click', (event) => {
                event.preventDefault();
                this.retrieve_only_chunks_value = this.retrieve_only_chunks_el.value === 'True';
                this.precise_chunking_value = this.precise_chunking_el.value === 'True';
                this.retrieve_limit_value = parseInt(this.retrieve_limit_el.value, 10);

                console.log("Advanced settings saved!");
                this.advancedSaveMsg_el.textContent = 'Saved!';
                this.advancedSaveMsg_el.classList.add('visible');
                setTimeout(() => {
                    this.advancedSaveMsg_el.classList.remove('visible');
                    this.advancedSaveMsg_el.textContent = '';
                }, 2000);
            });
        }

        // Event Listener for the entire Document Tree
        this.documents_container_el.addEventListener('click', (event) => {
            const target = event.target;

            // --- Logic for Expanding/Collapsing a folder ---
            // We check if the click was on the folder's top bar, but NOT on the checkbox itself.
            const folderTop = target.closest('.folder-top');
            if (folderTop && target.type !== 'checkbox') {
                const folderDiv = folderTop.closest('.folder');
                if (folderDiv) {
                    folderDiv.classList.toggle('open');
                    const folderName = folderDiv.dataset.folderName;
                    // Update our state
                    if (folderDiv.classList.contains('open')) {
                        this.openFolders.add(folderName);
                    } else {
                        this.openFolders.delete(folderName);
                    }
                }
            }

            // --- Logic for Checkboxes ---
            if (target.type === 'checkbox') {
                const folderNameFromDataset = target.dataset.folder;
                if (folderNameFromDataset) {
                    // It's a FILE checkbox
                    this.handleFileToggle(folderNameFromDataset, target.value, target.checked);
                } else if (target.closest('.folder-top')) {
                    // It's a FOLDER checkbox
                    this.handleFolderToggle(target.value, target.checked);
                }
            }

            // --- Logic for Delete Icon ---
            if (target.classList.contains('delete-icon')) {
                const { folder, file } = target.dataset;
                this.handleFileDelete(folder, file);
            }
        });

        // Event Listeners for Upload Form
        if (this.templateFolder_el) {
            this.templateFolder_el.addEventListener('change', () => this.handleFolderSelectionChange());
        }
        if (this.uploadForm_el) {
            this.uploadForm_el.addEventListener('submit', (event) => this.handleFileUpload(event));
        }

        // Event Listeners for Update Form
        if (this.updateForm_el) {
            this.updateForm_el.addEventListener('submit', (event) => this.handleFileUpdate(event));
        }

        // UPLOAD BUTTON LOGIC
        if (this.uploadButton_el) {
            this.uploadButton_el.addEventListener('click', (event) => {
                event.preventDefault();
                // If a file is already selected, this click will clear it.
                if (this.fileInput_el.files.length > 0) {
                    // Clear the selected file
                    this.fileInput_el.value = '';
                    // Manually trigger the 'change' event to update the UI via handleFileSelection
                    this.fileInput_el.dispatchEvent(new Event('change', { bubbles: true }));
                } else {
                    // Otherwise, it opens the file dialog.
                    this.fileInput_el.click();
                }
            });
        }
        // Listen for when a file is chosen in the hidden UPLOAD input
        if (this.fileInput_el) {
            this.fileInput_el.addEventListener('change', () => {
                this.handleFileSelection(this.fileInput_el, this.uploadButton_el, this.uploadFilename_el);
            });
        }

        // UPDATE BUTTON LOGIC
        if (this.updateButton_el) {
            this.updateButton_el.addEventListener('click', (event) => {
                event.preventDefault();
                if (this.updateFileInput_el.files.length > 0) {
                    this.updateFileInput_el.value = '';
                    this.updateFileInput_el.dispatchEvent(new Event('change', { bubbles: true }));
                } else {
                    this.updateFileInput_el.click();
                }
            });
        }
        // Listen for when a file is chosen in the hidden UPDATE input
        if (this.updateFileInput_el) {
            this.updateFileInput_el.addEventListener('change', () => {
                this.handleFileSelection(this.updateFileInput_el, this.updateButton_el, this.updateFilename_el);
            });
        }
    }

    handleFolderToggle(folderName, isChecked) {
        if (isChecked) {
            this.selectedDocuments[folderName] = [...this.documents[folderName]];
        } else {
            this.selectedDocuments[folderName] = [];
        }

        // --- Targeted Update ---
        // Find all file checkboxes within this folder and update their state
        const folderDiv = this.documents_container_el.querySelector(`[data-folder-name="${folderName}"]`);
        if (folderDiv) {
            const fileCheckboxes = folderDiv.querySelectorAll('.file input[type="checkbox"]');
            fileCheckboxes.forEach(checkbox => checkbox.checked = isChecked);
        }
        
        console.log('Updated Selection:', this.selectedDocuments);
    }

    handleFileToggle(folderName, fileName, isChecked) {
        const selection = this.selectedDocuments[folderName] || [];
        const fileIndex = selection.indexOf(fileName);

        if (isChecked && fileIndex === -1) {
            selection.push(fileName);
        } else if (!isChecked && fileIndex > -1) {
            selection.splice(fileIndex, 1);
        }
        this.selectedDocuments[folderName] = selection;

        // --- Targeted Update ---
        // Find the parent folder's checkbox and update its state
        const folderDiv = this.documents_container_el.querySelector(`[data-folder-name="${folderName}"]`);
        if (folderDiv) {
            const folderCheckbox = folderDiv.querySelector('.folder-top input[type="checkbox"]');
            const totalFiles = this.documents[folderName].length;
            const selectedFiles = this.selectedDocuments[folderName].length;
            
            // If all files are selected, check the folder. Otherwise, uncheck it.
            folderCheckbox.checked = totalFiles === selectedFiles;
        }

        console.log('Updated Selection:', this.selectedDocuments);
    }

    async handleFileDelete(folderName, fileName) {
        if (confirm(`Are you sure you want to delete "${fileName}"?`)) {
            
            this.spinner_el.classList.remove('hidden');

            try {
                const response = await fetch('/deletefile', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        folder: folderName,
                        filename: fileName,
                    }),
                });

                if (!response.ok) {
                    const errorText = await response.text();
                    throw new Error(`Server responded with ${response.status}: ${errorText}`);
                }
                console.log(`Successfully requested deletion for: ${folderName}/${fileName}`);

            } catch (error) {
                console.error('Failed to delete file:', error);
                alert(`An error occurred while trying to delete the file.\n\nError: ${error.message}`);
            } finally {
                this.spinner_el.classList.add('hidden');

                console.log("Re-syncing file list with the server...");
                await this.fetchDocuments();

                this.populateFolderDropdown();
                this.populateUpdateFolderDropdown();
                this.renderDocuments();
            }
        }
    }

    handleFolderSelectionChange() {
        const selectedValue = this.templateFolder_el.value;
        const isCreatingNew = selectedValue === 'Create a new one';

        // Toggle visibility based on selection
        this.newTemplateFolder_label.style.display = isCreatingNew ? 'block' : 'none';
        this.newTemplateFolder_input.style.display = isCreatingNew ? 'block' : 'none';

        // Make the input required only when it's visible
        this.newTemplateFolder_input.required = isCreatingNew;
    }

    async handleFileUpload(event) {
        event.preventDefault();
        console.log("Upload form submitted.");
        this.spinner_el.classList.remove('hidden');

        const formData = new FormData(this.uploadForm_el);

        if (formData.get('template_folder') === 'Create a new one') {
            const newFolderName = formData.get('new_template_folder');
            if (newFolderName) {
                formData.set('template_folder', newFolderName);
            }
        }
        
        formData.delete('new_template_folder');

        try {
            // Attempt to upload the file to the /uploadfile endpoint
            const response = await fetch('/uploadfile', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(`Upload failed! Server responded with ${response.status}: ${errorText}`);
            }

            console.log("File uploaded successfully!");
            alert("File uploaded successfully!");

        } catch (error) {
            console.error("Error uploading file:", error);
            alert(`File upload failed. Please try again.\nError: ${error.message}`);
        } finally {
            console.log("Re-syncing file list with the server...");
            await this.fetchDocuments();

            this.populateFolderDropdown();
            this.populateUpdateFolderDropdown();
            this.renderDocuments();
            
            this.spinner_el.classList.add('hidden');
            this.uploadForm_el.reset();
            this.handleFolderSelectionChange();

            this.uploadButton_el.classList.remove('file-selected');
            this.uploadFilename_el.textContent = '';
        }
    }

    async handleFileUpdate(event) {
        event.preventDefault();
        console.log("Update form submitted.");

        if (!this.updateFileInput_el.files || this.updateFileInput_el.files.length === 0) {
            alert("Please choose a file to update.");
            return;
        }

        this.spinner_el.classList.remove('hidden');

        const formData = new FormData(this.updateForm_el);
        
        try {
            const response = await fetch('/updatefile', {
                method: 'POST',
                body: formData, 
            });

            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(`Update failed! Server responded with ${response.status}: ${errorText}`);
            }

            console.log("File updated successfully!");
            alert("File updated successfully!");

        } catch (error) {
            console.error("Error updating file:", error);
            alert(`File update failed. Please try again.\nError: ${error.message}`);
        } finally {
            console.log("Re-syncing file list with the server...");
            await this.fetchDocuments();

            this.populateFolderDropdown();
            this.populateUpdateFolderDropdown();

            this.renderDocuments();
            this.spinner_el.classList.add('hidden');
            this.updateForm_el.reset();

            this.updateButton_el.classList.remove('file-selected');
            this.updateFilename_el.textContent = '';
        }
    }

    handleFileSelection(inputElement, buttonElement, filenameElement) {
        if (inputElement.files && inputElement.files.length > 0) {
            const fileName = inputElement.files[0].name;
            filenameElement.textContent = fileName;
            buttonElement.classList.add('file-selected');

        } else {
            filenameElement.textContent = '';
            buttonElement.classList.remove('file-selected');
        }
    }
}