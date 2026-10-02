此SKILL灵感来自于天才Agent少女ASu

# Resume Authoring

Skill package version: `v0.2.0`. Resume content, Word files and PDF files retain their own approval states.

This Skill guides evidence-based resume writing and revision across different candidates. It separates content-module confirmation, editable Word review, PDF acceptance, and versioned delivery. Each run reads only the current candidate's authorized materials in that candidate's private workspace; the package contains no candidate resume or personal template.

Invoke `$resume-authoring` when preparing or revising a resume. Provide the target role, audience, source materials, and any accepted prior version. The Skill will first establish the evidence and review boundaries, then work through sections before file production.

## 子 Skill：逐项目简历审核

[`resume-project-review`](skills/resume-project-review/SKILL.md) 提供完整原文与建议稿对照、逐项目审批、保留关键方案的压缩、反馈传播及中英文分阶段交付。父 Skill 在相应任务中加载它。

[中文文档检查](skills/resume-project-review/references/chinese-quality.md) 覆盖 UTF-8、真实加粗与链接、中文字体、文字读回、全页渲染和用户报告的查看器问题。检查脚本只读取调用者提供的文件，不包含个人简历或路径。
