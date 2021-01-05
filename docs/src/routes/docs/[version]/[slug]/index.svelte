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
    import hljs from "highlight.js";
    import { onMount } from "svelte";

    export let docs: {
        content: string;
        matter: { title: string; order: number; slug: string };
    };

    onMount(() => {
        document.querySelectorAll("pre code").forEach((el) => {
            hljs.highlightBlock(el as HTMLElement);
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
    });
</script>

<h1 class="w3-xxxlarge">{docs.matter.title}</h1>
<hr class="w3-border-top w3-border-black" />

<div class="w3-padding">
    {@html marked(docs.content)}
</div>
