# 颐护小护 · 智慧陪护（可安装离线网页应用）

面向独居老人的多模态智慧陪护 App，按「颐护家园」网站的视觉与内容组织方式做成一个
可安装、可离线使用的 PWA（渐进式网页应用）。整个应用只有静态文件，不需要服务器、
不需要联网，也不采集任何个人信息。

- 首页：品牌区、首屏标语、九项能力卡片、智能终端系统入口
- 详情页：每个模块独立说明页（问题背景 / 工作原理 / 关键参数 / 适用场景），配矢量插画
- 终端页：应用内用 iframe 加载树莓派控制台 `http://192.168.43.9:8000/`，连不上时给出兜底提示

## 一、怎么部署

> 完整步骤见 [DEPLOY.md](DEPLOY.md)：支持网页拖拽上传、GitHub Actions 自动部署、`deploy.py` 一键部署。

## 二、怎么打开

| 方式 | 做法 | 说明 |
|---|---|---|
| 直接打开 | 双击 `index.html` | 能看全部内容与详情页；Service Worker 不生效（file:// 限制） |
| 本地服务器（推荐测试） | 在目录下执行 `python -m http.server 8000`，访问 `http://127.0.0.1:8000` | 可安装、可离线 |
| 部署到网上（推荐分发） | 上传整个文件夹到 GitHub Pages / 任意静态托管，用 HTTPS 访问 | 可安装、可离线、可分享链接 |

## 三、怎么“安装”到手机（像 App 一样）

**Android（Chrome / Edge）**
1. 用浏览器打开部署后的网址
2. 右上角菜单 →「添加到主屏幕」/「安装应用」
3. 桌面出现绿色小护图标，点开全屏运行，断网也能用

**iPhone（Safari）**
1. 用 Safari 打开网址
2. 底部「分享」→「添加到主屏幕」
3. 桌面出现图标，点开即为全屏应用

安装后首次打开会缓存全部资源，之后即使断网也能正常浏览九项能力与详情页；
只有「智能终端系统」需要手机与树莓派在同一 Wi-Fi 才能打开。

## 四、改内容

| 想改什么 | 改哪里 |
|---|---|
| 应用名、标语、树莓派地址 | `assets/js/data.js` 顶部的 `APP` |
| 九个模块的名称、简介、详情文案、参数、场景 | `assets/js/data.js` 里的 `MODULES` 数组 |
| 配色、字号、间距 | `assets/css/style.css` 顶部 `:root` 变量 |
| 插画 / 图标 | `assets/img/` 下的 SVG，或改 `gen_assets.py` 重新生成 |
| 应用图标 | `assets/icons/icon-192.png`、`icon-512.png` |

> 新增模块：在 `MODULES` 里加一项（含 `id`、`name`、`short`、`lead`、`problem`、
> `steps`、`specs`、`scenes`），再补 `assets/img/icon-新id.svg` 与 `hero-新id.svg`，
> 首页和详情页会自动出现。

## 五、目录结构

```
yihu-app/
├── index.html               首页
├── module.html              模块详情（?id=xxx）
├── terminal.html            智能终端系统（iframe）
├── manifest.json            安装配置
├── sw.js                    离线缓存
├── favicon.png
├── assets/
│   ├── css/style.css
│   ├── js/data.js           全部内容数据
│   ├── js/app.js            首页渲染
│   ├── js/module.js         详情页渲染
│   ├── js/terminal.js       终端页逻辑
│   ├── img/                 图标与插画（SVG）
│   └── icons/               安装图标（PNG）
├── gen_assets.py            插画与图标生成脚本
└── README.md
```

## 六、关于终端系统

- 地址写在 `data.js` 的 `APP.terminalUrl`，默认 `http://192.168.43.9:8000/`
- 页面内用 iframe 加载，若树莓派服务未启动、手机不在同一 Wi-Fi，或浏览器禁止混合内容，
  会显示兜底提示，可「用浏览器打开」或「复制地址」
- 注意：如果本应用部署在 HTTPS 站点上，浏览器通常会拦截 `http://` 的 iframe（混合内容）。
  此时请用兜底里的「用浏览器打开」，或把设备端也配置成 HTTPS

## 七、隐私

应用不含任何统计、埋点、第三方请求；所有内容随包分发，数据不离开本机。
页面底部不展示手机号、邮箱等个人信息。
