import rehypeStringify from "rehype-stringify";
import remarkFrontmatter from "remark-frontmatter";
import remarkGfm from "remark-gfm";
import remarkParse from "remark-parse";
import remarkRehype from "remark-rehype";
import { unified } from "unified";
import { matter } from "vfile-matter";

export async function parseMarkdown(md: string) {
  const parsed = await unified()
    .use(remarkParse)

    // parse frontmatter
    .use(remarkFrontmatter)
    .use(() => (_, file) => matter(file))

    // autolink literals, footnotes, strikethrough, tables, tasklists
    .use(remarkGfm)

    // convert to HTML tree
    .use(remarkRehype)

    // convert tree to string
    .use(rehypeStringify)

    .process(md);

  return [parsed.data.matter, String(parsed)];
}
