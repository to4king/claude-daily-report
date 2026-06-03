#!/usr/bin/env node
/**
 * HTML → PDF 変換スクリプト
 * Playwright/Chromium を使用
 *
 * 使用方法:
 *   node html_to_pdf.js <input.html> <output.pdf>
 *
 * 注意:
 *   生成される PDF は約 1MB になるため Drive MCP への直接アップロードは困難。
 *   現状は HTML 形式での Drive 保存を推奨。
 *   PDF が必要な場合は Ghostscript 等で圧縮するか Google Apps Script 経由を検討。
 */

const { chromium } = require("playwright");
const path = require("path");
const fs = require("fs");

async function htmlToPdf(inputPath, outputPath) {
  const absoluteInput = path.resolve(inputPath);

  if (!fs.existsSync(absoluteInput)) {
    console.error(`入力ファイルが見つかりません: ${absoluteInput}`);
    process.exit(1);
  }

  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.goto(`file://${absoluteInput}`, { waitUntil: "networkidle" });

  await page.pdf({
    path: outputPath,
    format: "A4",
    margin: { top: "20mm", right: "15mm", bottom: "20mm", left: "15mm" },
    printBackground: true,
  });

  await browser.close();
  console.log(`PDF を生成しました: ${outputPath}`);
}

const [, , input, output] = process.argv;
if (!input || !output) {
  console.error("使用方法: node html_to_pdf.js <input.html> <output.pdf>");
  process.exit(1);
}

htmlToPdf(input, output).catch((err) => {
  console.error("PDF 変換エラー:", err);
  process.exit(1);
});
