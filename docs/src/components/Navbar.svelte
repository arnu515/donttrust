<script lang="ts">
    import versions from "../../content/docs_version.json";

    let version = versions[0];
    export let sidebar = false;
</script>

<div class="w3-bar w3-blue w3-border-bottom w3-border-black">
    <button
        class="w3-bar-item w3-button w3-hover-blue"
        on:click={() => (sidebar = !sidebar)}><i
            class="fas fa-{sidebar ? 'times' : 'bars'}" /></button>
    <a href="/docs" class="w3-bar-item w3-button w3-hover-blue">DontTrust Docs</a>
    <select
        bind:value={version}
        class="w3-bar-item w3-select w3-border-black w3-white"
        on:input={() => (window.location.href = '/docs/' + version)}>
        {#each versions as v}
            <option value={v}>{v}</option>
        {/each}
    </select>
    <div class="w3-right">
        <a
            class="w3-bar-item w3-button w3-hover-blue w3-hover-text-light-gray"
            href="https://github.com/arnu515/donttrust/tree/master/docs">Github</a>
    </div>
</div>
