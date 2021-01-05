<script lang="ts">
    export let status: number;
    export let error: Error;

    const dev = process.env.NODE_ENV === "development";
</script>

<svelte:head>
    <title>An error occured - {status}</title>
</svelte:head>

<h1 class="w3-center w3-jumbo">{status}</h1>

<p class="w3-center w3-large">{error.message}</p>

{#if dev && error.stack}
    <pre
        class="w3-border w3-light-gray w3-border-black w3-rounded w3-padding">
		{error.stack}
	</pre>
{/if}
