export default class Sources {
    constructor() {
        this.sources_map = new Map(); // dict[int, dict] -> It's a mapping from message ids to sources dics
        this.sources_counter = 0
    }

    add_new_sources(sources) {
        const new_id = this.sources_counter;
        const organized_sources = this.organize_chunks(sources);
        this.sources_map.set(new_id, organized_sources);
        this.sources_counter++;
        return new_id;
    }

    organize_chunks(sources) {
        const organized_sources = {};
        sources.forEach(el => {
            const document_name = el["document_name"];
            const quote = el["quote"];

            if (document_name in organized_sources) {
                organized_sources[document_name].push(quote);
            } else {
                organized_sources[document_name] = [quote];
            }
        });
        return organized_sources;
    }

    get_sources_by_id(id) {
        return this.sources_map.get(id);
    }

    get_sources_html_by_id(id) {
        const sources = this.get_sources_by_id(id);

        // Handle the case where no sources are found for this ID
        if (!sources || Object.keys(sources).length === 0) {
            return '<p>No sources provided for this response.</p>';
        }

        let filesHtml = '';

        for (const document_name in sources) {
            // Create a clean name by removing the .md extension.
            const cleanName = document_name.replace(/\.md$/, '');

            const pathForUrl = cleanName.startsWith('/') ? cleanName.substring(1) : cleanName;
            const fileUrl = `http://localhost:3001/getfile/${encodeURIComponent(pathForUrl)}`;

            filesHtml += '<div class="file-chunks-container">';
            filesHtml += `<a href="${fileUrl}" target="_blank"">${cleanName}</a>`;
            filesHtml += '<div class="file-chunks-container-2">';

            const quotes = sources[document_name];

            quotes.forEach((quote, index) => {
                const sanitized_quote = quote.replace(/</g, "&lt;").replace(/>/g, "&gt;");
                
                filesHtml += '<div class="file-chunk-container">';
                filesHtml += `<h4>Chunk ${index + 1}</h4>`;
                filesHtml += '<div class="file-chunk-container-2">';
                filesHtml += `<span>${sanitized_quote}</span>`;
                filesHtml += '</div>';
                filesHtml += '</div>';
            });

            filesHtml += '</div>';
            filesHtml += '</div>';
        }

        return filesHtml;
    }
}