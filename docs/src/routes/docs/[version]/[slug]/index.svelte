<script lang="ts" context="module">
    import versions from "../../../../../content/docs_version.json";

    export async function preload({ params: { version, slug } }) {
        if (!versions.includes(version))
            this.error(404, "Docs version not found");

        try {
            const res = await this.fetch(`/docs/${version}/${slug}.json`);
            const data = await res.json();
            if (data.success) return { docs: data.data, version };
            else this.error(res?.status || 500, data.message);
        } catch (e) {
            this.error(500, e);
        }
    }
</script>

<script lang="ts">
    import marked from "marked";
    import prism from "prismjs";
    import { afterUpdate, getContext } from "svelte";
    import EditThisPageOnGithub from "../../../../components/EditThisPageOnGithub.svelte";

    import "prismjs/components/prism-python";
    import "prismjs/components/prism-bash";
    import "prismjs/plugins/autolinker/prism-autolinker";
    import "prismjs/plugins/line-numbers/prism-line-numbers";

    export let docs: {
        content: string;
        matter: {
            title: string;
            order: number;
            slug: string;
            description: string;
            keywords: string;
        };
    };
    export let version: string;
    const items = getContext<typeof docs[]>("items");

    let href = "/";

    afterUpdate(() => {
        code();
        if (typeof window !== "undefined")
            href = `https://github.com/arnu515/donttrust/tree/master/docs/content${window.location.pathname.replace(
                "/docs",
                ""
            )}.md`;
    });

    function code() {
        if (typeof document === "undefined") {
            return;
        }

        document.querySelectorAll("pre code").forEach((el) => {
            prism.highlightElement(el);
        });

        document.querySelectorAll("pre").forEach((el) => {
            const button = document.createElement("button");
            button.className =
                "w3-button w3-border w3-border-black w3-hover-blue w3-hover-text-light-gray";
            button.textContent = "Copy";
            button.style.fontSize = "14px";
            button.style.padding = "3px 6px";
            button.style.margin = "5px";

            el.style.position = "relative";
            button.style.position = "absolute";
            button.style.right = "0";
            button.style.top = "0";

            button.addEventListener("click", () => {
                const textarea = document.createElement("textarea");
                textarea.value = el.textContent.endsWith("Copy")
                    ? el.textContent.slice(0, el.textContent.length - 4)
                    : el.textContent;
                document.body.appendChild(textarea);
                textarea.select();
                document.execCommand("copy");
                textarea.remove();
            });

            el.appendChild(button);
        });
    }
</script>

<svelte:head>
    <title>{docs.matter.title}</title>
    <meta name="description" content={docs.matter.description} />
    <meta name="keywords" content={docs.matter.keywords} />
</svelte:head>

<h1 class="w3-xxxlarge">{docs.matter.title}</h1>
<p>{docs.matter.description}</p>
<hr class="w3-border-top w3-border-black" />

{@html marked.parseInline(docs.content, { gfm: true, breaks: false })}

<EditThisPageOnGithub {href} />

<div class="w3-row-padding">
    {#if items.find((i) => i.matter.order === docs.matter.order - 1)}
        <div class="w3-col s12 m6">
            <a
                style="text-decoration: none"
                href="/docs/{version}/{items.find((i) => i.matter.order === docs.matter.order - 1).matter.slug}">
                <div
                    class="w3-panel w3-border w3-leftbar w3-border-black w3-padding">
                    <h5 style="margin: 0" class="w3-large">Previous</h5>
                    <p style="margin: 0" class="w3-text-gray">
                        {items.find((i) => i.matter.order === docs.matter.order - 1).matter.title}
                    </p>
                </div>
            </a>
        </div>
    {:else}
        <div class="w3-col s12 m6">&nbsp;</div>
    {/if}
    {#if items.find((i) => i.matter.order === docs.matter.order + 1)}
        <div class="w3-col s12 m6">
            <a
                style="text-decoration: none"
                href="/docs/{version}/{items.find((i) => i.matter.order === docs.matter.order + 1).matter.slug}">
                <div
                    class="w3-panel w3-border w3-rightbar w3-border-black w3-padding">
                    <h5 class="w3-large" style="margin: 0">Next</h5>
                    <p class="w3-text-gray" style="margin: 0">
                        {items.find((i) => i.matter.order === docs.matter.order + 1).matter.title}
                    </p>
                </div>
            </a>
        </div>
    {:else}
        <div class="w3-col s12 m6">&nbsp;</div>
    {/if}
</div>
