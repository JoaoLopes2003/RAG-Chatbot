export default class Sources {
    constructor() {
        this.sources_map = {} // dict[int, dict] -> It's a mapping from message ids to sources dics
        this.current_id = None
        this.sources_counter = 0
    }

    add_new_sources(sources) {
        this.sources_map.push({
            key:   this.current_id,
            value: sources
        })
        this.sources_counter++
    }
}