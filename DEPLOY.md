# 部署到 GitHub Pages（让应用可以“安装”）

`yihu-app` 就是一个纯静态站点，放到任何 **HTTPS** 静态托管上都能用；
只有 HTTPS（或 localhost）环境下浏览器才允许“安装到桌面”和离线缓存。

下面三种方式任选一种，**方式 A 最简单，不需要装任何工具**。

---

## 方式 A：网页拖拽上传（推荐，约 2 分钟）

1. 打开 GitHub，新建仓库：右上角 **+ → New repository**
   - Repository name 填 `yihu-app`（或任意名字）
   - 选 **Public**（Private 仓库要付费才能开 Pages）
   - 不要勾选 “Add a README file”
   - 点 **Create repository**
2. 进入仓库，点 **uploading an existing file**（或 Add file → Upload files）
3. 把 `yihu-app` 文件夹里的**全部内容**拖进去
   - 包括 `index.html`、`assets`、`.github`、`.nojekyll`、`manifest.json` 等
   - 注意：要拖文件夹**里面**的东西，不要拖 `yihu-app` 这一层，否则网址会多一层路径
4. 底部点 **Commit changes**
5. 仓库 → **Settings → Pages**
   - Source 选 **Deploy from a branch**
   - Branch 选 `main`，目录选 `/ (root)`
   - 点 **Save**
6. 等 1–2 分钟，页面顶部会出现网址：
   `https://<你的用户名>.github.io/yihu-app/`
7. 用手机打开这个网址：
   - **Android Chrome**：菜单 →「安装应用」/「添加到主屏幕」
   - **iPhone Safari**：分享 →「添加到主屏幕」

> 如果上传时漏了 `.github` 或 `.nojekyll` 也没关系，它们不是运行必需：
> `.nojekyll` 只是避免 GitHub 用 Jekyll 处理文件，`.github` 是自动部署用的。

---

## 方式 B：自动部署（改代码后自动更新）

适合以后要持续修改的情况：

1. 按方式 A 建好仓库并上传文件（`.github/workflows/pages.yml` 会一起传上去）
2. 仓库 → **Settings → Pages** → Source 选 **GitHub Actions**
3. 之后每次 `git push` 到 `main`，Actions 会自动构建并发布
4. 在 **Actions** 标签页能看到部署进度

> 用这种方式时，Pages 的 Source 必须选 “GitHub Actions”，不要再选 branch，
> 否则两者会互相覆盖。

---

## 方式 C：一条命令部署（有 GitHub 令牌时）

不用装 git，直接跑脚本：

```bash
# 1) 生成令牌：GitHub → Settings → Developer settings
#    → Personal access tokens → Fine-grained tokens → Generate new token
#    权限勾选：Contents: Read and write、Pages: Read and write、Administration: Read and write
# 2) 运行
python deploy.py --token ghp_xxxxxxxx --repo yihu-app
```

脚本会自动：创建仓库（若不存在）→ 逐个上传文件 → 开启 Pages → 打印访问地址。

部署完成后地址形如 `https://<用户名>.github.io/yihu-app/`。

---

## 安装到手机后的效果

- 桌面出现绿色小护图标，点开全屏运行，没有浏览器地址栏
- 首次打开会缓存全部资源，之后**断网也能浏览**六个模块与详情页
- 只有「智能终端系统」需要手机与树莓派在同一个 Wi-Fi

## 常见问题

| 现象 | 原因与处理 |
|---|---|
| 打开是 404 | 文件多套了一层目录。仓库根目录应该直接看到 `index.html` |
| 页面能开但无法安装 | 必须 HTTPS；`github.io` 默认就是 HTTPS，检查是否用了 `http://` |
| 安装后仍是旧内容 | Service Worker 缓存。设置里清除站点数据，或把 `sw.js` 里的 `CACHE` 版本号改一下 |
| 终端系统白屏 | 手机不在同一 Wi-Fi；或页面是 HTTPS 而设备是 HTTP（混合内容被拦），用兜底页的「用浏览器打开」 |
| 图标不显示 | 确认 `assets/icons/icon-192.png`、`icon-512.png` 已上传 |
| 修改后不生效 | 等 1–2 分钟 Pages 构建；强制刷新（Ctrl/Cmd + Shift + R） |
