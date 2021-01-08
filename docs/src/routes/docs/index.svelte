<script lang="ts">
    import { onMount } from "svelte";
    import versions from "../../../content/docs_version.json";

    onMount(() => {});
</script>

<h1 class="w3-jumbo w3-center">DontTrust Docs</h1>

<ul
    class="w3-container w3-center w3-margin w3-large"
    style="list-style-type: none; width: auto">
    <h3>Versions</h3>
    {#each versions as version}
        <li>
            <a
                href="/docs/{version}"
                class="w3-button w3-margin-bottom w3-blue">{version}</a>
        </li>
    {/each}
    <li><a href="https://donttrust-apiref.vercel.app">API Reference</a></li>
</ul>
