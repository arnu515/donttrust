import type { ClientRequest, ServerResponse } from "http";
import versions from "../../../../content/docs_version.json";
import greyMatter from "gray-matter";
import fs from "fs";
import path from "path";

export function get(req: ClientRequest, res: ServerResponse) {
    res.setHeader("Content-Type", "application/json");

    const { version } = req["params"];
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

    try {
        const dir = fs
            .readdirSync(path.resolve("content", version))
            .filter((x) => x.endsWith(".md"));
        const data = dir.map((x) => {
            return {
                filename: x,
                matter: greyMatter(
                    fs.readFileSync(path.resolve("content", version, x))
                ).data,
            };
        });
        res.statusCode = 200;
        return res.end(
            JSON.stringify({
                success: true,
                message: "Files",
                data,
            })
        );
    } catch (err) {
        console.log(err);
        res.statusCode = 500;
        return res.end(
            JSON.stringify({
                success: false,
                message: JSON.stringify(err),
                data: { error: err },
            })
        );
    }
}
