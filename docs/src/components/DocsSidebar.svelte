<script lang="ts">
    import { fade } from "svelte/transition";

    interface Item {
        id: string | number;
        title: string;
        path: string;
        order: number;
    }

    export let items: Item[];
    export let active: string | number;
</script>

<div
    class="w3-sidebar w3-bar-block w3-card w3-animate-left"
    style="max-width: 350px;"
    out:fade>
    <h3 class="w3-bar-item">Docs</h3>

    {#each items.sort((x, y) => x.order - y.order) as { path, title, id }}
        <a
            href={path}
            class="w3-button w3-hover-white {id === active ? 'w3-text-blue w3-hover-text-cyan' : 'w3-text-dark-gray w3-hover-text-black'}">{title}</a>
    {/each}
    <a
        href="https://donttrust-apiref.vercel.app"
        class="w3-button w3-hover-white w3-text-dark-gray w3-hover-text-black">API
        Reference</a>
</div>
