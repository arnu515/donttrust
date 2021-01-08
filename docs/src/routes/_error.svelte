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

<p class="w3-center"><a href="/">Homepage</a></p>
{#if status !== 404}
    <p class="w3-center">
        <button class="w3-button w3-blue w3-hover-blue">Reload page</button>
    </p>
{/if}

{#if dev && error.stack}
    <pre
        class="w3-border w3-light-gray w3-border-black w3-rounded w3-padding">
		{error.stack}
	</pre>
{/if}
