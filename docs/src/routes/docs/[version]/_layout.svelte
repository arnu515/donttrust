<script lang="ts" context="module">
    import versions from "../../../../content/docs_version.json";

    export async function preload({ params: { version }, path }) {
        if (!versions.includes(version))
            this.error(404, "Docs version not found");

        try {
            const res = await this.fetch(`/docs/${version}.json`);
            const data = await res.json();
            const active = path.split("/")[path.split("/").length - 1];
            if (data.success) return { data: data.data, version, active };
            else this.error(res?.status || 500, data.message);
        } catch (e) {
            this.error(500, e);
        }
    }
</script>

<script lang="ts">
    import { setContext } from "svelte";
    import DocsSidebar from "../../../components/DocsSidebar.svelte";
    import Navbar from "../../../components/Navbar.svelte";

    let sidebar = false;
    export let version: string;
    export let active: string;
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

    setContext("items", data);
</script>

<Navbar bind:sidebar />

{#if sidebar}
    <DocsSidebar
        items={data.map((x) => {
            return { id: x.matter.slug, path: `/docs/${version}/${x.matter.slug}`, title: x.matter.title };
        })}
        {active} />
{/if}

<div class="w3-container">
    <slot />
</div>
