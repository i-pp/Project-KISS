# Project-KISS

**Keep It Simple, Stupid.**

複雑なものを、複雑なまま人間に押し付けない。

Project-KISSは、単純で、部品を置き換えられ、進化を続けられるシステムを作るための設計思想と全体構想を扱う。

## 設計原則

- 必要な複雑さは適切な層が引き受け、利用者・開発者・運用者の負担を減らす。
- 責務とインターフェースを分け、各部品を独立して改善・交換できる構造にする。
- 最小の意味ある実装を動かし、観測・測定・独立した検証をもとに判断する。
- 変更の根拠と結果を記録し、必要なときに戻せるようにする。
- 利用者の自由と制御を守り、作る楽しさと使う楽しさを両立する。

## この思想を基に作るもの

[Project-AceIS](https://github.com/orgs/i-pp/projects/2)をProject-KISSの管理下に置き、AceISとACE・PAUL・GENE・PETERの設計・実装・検証を進める。

AceISは、各コンポーネントを包含する統合システム。推論・検証・自己改善、プログラム解析、ネイティブコード生成、移植・変換の責務を分けて構成する。詳細な仕様と実装上の境界はDraft設計書の検討事項とする。

## Draft設計書

- [設計思想・構想統合設計書 第5版ドラフト](docs/Project-KISS_design_v5_draft.md)

本リポジトリは文書専用とし、実装コードや実験ログは置かない。設計書の方針・提案・保留・未検証事項は、完成済み仕様や性能保証として扱わない。

第5版本文に残る「Project-ACE」は、現在GitHub上で「Project-AceIS」として管理するサブプロジェクトの旧表記。第5版の原文は改変せず保存している。

AceGeneralPublicLicenseは設計構想中の名称であり、第5版はライセンス条文を代替しない。利用条件は別途確定する。

## プロジェクト管理

- [Project-KISS](https://github.com/orgs/i-pp/projects/1)
- [Project-AceIS](https://github.com/orgs/i-pp/projects/2)

GitHub Projects間の管理関係は、相互リンクとこの文書で表す。
