<script lang="ts" context="module">
    import versions from "../../../../content/docs_version.json";

    export async function preload({ params: { version } }) {
        if (!versions.includes(version))
            this.error(404, "Docs version not found");

        try {
            const res = await this.fetch(`/docs/${version}.json`);
            const data = await res.json();
            if (data.success) return { data: data.data, version };
            else this.error(res?.status || 500, data.message);
        } catch (e) {
            this.error(500, e);
        }
    }
</script>

<script lang="ts">
    export let version: string;
    export let data: {
        filename: string;
        matter: {
            title: string;
            order: number;
            slug: string;
            description: string;
            keywords: string;
        };
    }[];
</script>

<svelte:head>
    <title>DontTrust's Documentation</title>
</svelte:head>

<h1 class="w3-jumbo" style="margin-bottom: 0">DontTrust's Documentation</h1>
<p class="w3-xlarge w3-text-dark-gray" style="margin-top: 0">
    version
    {version}
</p>

<h3>Table of contents:</h3>
<ul>
    {#each data.sort((x, y) => {
        return x.matter.order - y.matter.order;
    }) as { matter: { title, slug } }}
        <li><a href="/docs/{version}/{slug}">{title}</a></li>
    {/each}
    <li><a href="/apiref/index.html">API Reference</a></li>
</ul>
