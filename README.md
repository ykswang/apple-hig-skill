# apple-design

把 Apple [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines) 全站 173 个页面提炼成一个 Agent Skill（`skills/apple-hig`），供 Claude 或其他 AI 在设计、编写、评审 Apple 平台 UI 时按需加载、遵循。

内容版本：抓取于 2026-09-25，HIG 最新变更为 2026 年 9 月（含 Liquid Glass、iPhone Duo、Apple In-App Purchase）。

## 结构

```
skills/apple-hig/
├── SKILL.md                 # 入口：使用流程、8 大设计原则、跨页面硬性规则（尺寸/对比度/字号）、任务→文件路由表、评审清单
└── references/
    ├── INDEX.md             # 全部 158 个页面的一行摘要索引，按官网左侧菜单顺序排列
    ├── getting-started/     # 设计原则 + 各平台（iOS/iPadOS/macOS/watchOS/tvOS/visionOS/游戏/iPhone Duo）
    ├── foundations/         # 颜色、排版、布局、材质、SF Symbols、图标、无障碍、隐私……
    ├── patterns/            # 加载、引导、搜索、设置、模态、拖放、撤销……
    ├── components/          # 所有系统组件（按钮、菜单、工具栏、标签栏、sheet、alert、widget……）
    ├── inputs/              # 手势、键盘、指针、眼动、Apple Pencil、Digital Crown……
    └── technologies/        # Apple Pay、Sign in with Apple、Wallet、Siri、CarPlay、HealthKit……
tools/
├── crawl.py                 # 通过 DocC JSON 接口抓取全站并渲染为 Markdown
├── DISTILL_SPEC.md          # 提炼规范（每页 → 参考文件的格式与保真规则）
├── build_index.py           # 生成 references/INDEX.md
└── verify.py                # 校验：参考文件齐全、原文数值规格全部保留、规则条数对照
```

参考文件为英文，与原文术语保持一致，便于 AI 精确匹配 API 名和组件名。每个文件的结构一致：适用场景 → 规则（保留 Apple 原文的 Never/Avoid/Prefer/Consider 强度）→ 平台差异 → 规格数值 → API → 相关页面。

## 安装

```bash
# Claude Code（全局）
ln -s "$PWD/skills/apple-hig" ~/.claude/skills/apple-hig
# 或仅对某个项目生效
ln -s "$PWD/skills/apple-hig" <project>/.claude/skills/apple-hig
```

其他 AI：把 `SKILL.md` 作为系统提示/上下文，并允许其按路由表读取 `references/` 下的文件。

## 更新

```bash
python3 tools/crawl.py /tmp/hig                  # 重新抓取原文 → /tmp/hig/raw/*.md + pages.json
# 按 tools/DISTILL_SPEC.md 重新提炼有变化的页面（对比新旧 raw 即可定位）
python3 tools/build_index.py /tmp/hig skills/apple-hig
python3 tools/verify.py /tmp/hig skills/apple-hig
```

## 已知说明

- 当前 HIG 的 Layout 页已不再提供按设备的屏幕尺寸表（仅 change log 中残留提及）；Widget 与 Live Activity 页仍保留按设备的尺寸。
- 部分表格中的数值疑似 Apple 原文笔误（如 complications 的 “18x18x pt”、typography 中个别 leading/tracking 值），已按原文照录，未做修正。
- 各参考文件的 APIs 段只包含原文中实际链接到的开发者文档名称。
