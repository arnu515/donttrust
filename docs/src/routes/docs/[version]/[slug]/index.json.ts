import type { ClientRequest, ServerResponse } from "http";
import versions from "../../../../../content/docs_version.json";
import greyMatter from "gray-matter";
import fs from "fs";
import path from "path";
import marked from "marked";

export function get(req: ClientRequest, res: ServerResponse) {
    res.setHeader("Content-Type", "application/json");

    const { version, slug } = req["params"];
    if (!versions.includes(version)) {
        res.statusCode = 404;
        return res.end(
            JSON.stringify({
                success: false,
                message: "Docs version not found",
                data: {},
            })
        );
    }

    if (!fs.existsSync(path.resolve("content", version, `${slug}.md`))) {
        res.statusCode = 404;
        return res.end(
            JSON.stringify({
                success: false,
                message: "File not found",
                data: {},
            })
        );
    }

    const { content: raw, data: matter } = greyMatter(
        fs.readFileSync(path.resolve("content", version, `${slug}.md`))
    );
    const content = marked(raw);

    res.statusCode = 200;
    return res.end(
        JSON.stringify({
            success: true,
            message: "Found",
            data: { content, raw, matter },
        })
    );
}
