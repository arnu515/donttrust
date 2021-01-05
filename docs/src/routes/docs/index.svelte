<script lang="ts">
    import { onMount } from "svelte";

    import versions from "../../../content/docs_version.json";
    console.log(versions);

    onMount(() => {
        window.location.assign(`/docs/${versions[0]}`);
    });
</script>

<h1 class="w3-jumbo w3-center">Redirecting to latest docs</h1>
