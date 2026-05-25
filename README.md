# chinese-solar-terms-calendar-ics

苹果虽然拥有自带的「中国大陆节假日」日历，但是无法单独显示二十四节气。本项目提供了可订阅的 `.ics` 文件以解决此问题。

## 订阅链接

```text
https://watawata39.github.io/chinese-solar-terms-calendar-ics/solar_terms_2000_2100.ics
```

---

## 支持范围

- 二十四节气
- 时间范围：2000 年 - 2100 年
- 全天事件（All-day Events）
- 兼容 Apple Calendar / Google Calendar / Outlook 等支持 `.ics` 订阅的日历应用

---

## Apple 日历订阅方法

### macOS

打开「日历」应用：

```text
文件 → 新建日历订阅
```

粘贴订阅链接即可。

### iPhone / iPad

打开：

```text
设置 → 日历 → 账户 → 添加账户 → 其他 → 添加已订阅的日历
```

然后输入订阅链接。

---

## 数据来源

本项目使用 Python 与 [`sxtwl`](https://pypi.org/project/sxtwl/) 生成节气数据。

---

## 生成方式

安装依赖：

```bash
pip install sxtwl
```

运行脚本：

```bash
python generate_solar_terms_ics.py
```

---

## License

MIT