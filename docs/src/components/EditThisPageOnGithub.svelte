<script lang="ts">
    import { onMount } from "svelte";

    let href = "/";

    onMount(() => {
        href = `https://github.com/arnu515/donttrust/tree/master/docs/content${window.location.pathname.replace(
            "/docs",
            ""
        )}.md`;
    });
</script>

<p class="w3-text-gray">
    <a {href}> <i class="fab fa-github" /> Edit this page on Github</a>
</p>
