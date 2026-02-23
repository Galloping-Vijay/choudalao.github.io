---
title: "解决 WSL2 + Windows Hosts + 开启 VPN 后无法访问本地 Web 服务的问题"
date: 2026-01-19T17:04:39+08:00
updated: 2026-02-23T21:03:34+08:00
author: "臭大佬"
categories: [linux]
description: "解决 WSL2 + Windows Hosts + 开启 VPN 后无法访问本地 Web 服务的问题"
cover: "https://www.choudalao.com/images/config/default-img.jpg"
click: 428
---

## 问题
> **场景描述**：
> - 你在 **WSL2 中运行了一个 Web 服务（如 Nginx、Go、Php、Node.js 等）**。
> - 在 **Windows 的 `hosts` 文件中绑定了域名（如 `dev.wsl.net -> 172.x.x.x`）**，以便在 Windows 浏览器中访问该服务。
> - **不开 VPN 时一切正常**，但一旦开启公司或个人的 **全流量接管型 VPN**，Windows 就无法解析该域名，导致页面打不开。

本文将详细介绍这个问题的原因，并提供一个简单有效的解决方案：**使用 `.localhost` 域名**。

---

## 🔍 问题描述

### ✅ 正常情况
- WSL2 中运行的 Web 服务可以通过绑定的域名（如 `http://dev.wsl.net`）从 Windows 浏览器访问。
- 例如，在 Windows 的 `hosts` 文件中有如下配置：
  ```text
  172.28.123.45 dev.wsl.net
  ```

### ❌ 开启 VPN 后
- 开启公司或个人的 **全流量接管型 VPN** 后，尝试访问 `http://dev.wsl.net` 会失败，提示“无法访问此网站”或 DNS 解析失败。

---

## 🛠️ 导致问题的原因

### 1. **VPN 劫持了所有 DNS 请求**
许多企业级或安全型 VPN（如 Cisco AnyConnect、Palo Alto GlobalProtect、OpenVPN 全隧道模式）会：
- **强制所有 DNS 查询走远程服务器**；
- **忽略或绕过本地 `C:\Windows\System32\drivers\etc\hosts` 文件**；
- 启用 **DNS over HTTPS (DoH)**，进一步跳过本地解析。

### 2. **结果**
当开启 VPN 后：
- 访问 `dev.wsl.net` → 不再查 hosts → 发送 DNS 请求到远程 → 远程返回“不存在” → **访问失败 ❌**

---

## ✅ 解决方案：使用 `.localhost` 域名

根据 [RFC 6761](https://datatracker.ietf.org/doc/html/rfc6761)，**`.localhost` 域名必须解析为回环地址，且不得通过网络 DNS 查询**。因此，它不会被任何远程 DNS 或 DoH 影响。

### 操作步骤：

#### 1. **修改 Windows 的 `hosts` 文件**
以管理员身份打开 `C:\Windows\System32\drivers\etc\hosts`，将原来的：
```text
172.28.123.45 dev.wsl.net
```
改为：
```text
172.28.123.45 wsl.localhost
```

#### 2. **保存文件**

#### 3. **在 Windows 浏览器中访问**
```
http://wsl.localhost
```

#### 4. **现在，无论是否开启 VPN，都能正常访问！✅**

---

### 🧪 验证方法

在开启 VPN 的状态下，在 Windows 中执行：
```cmd
ping wsl.localhost
```
如果返回的是你的 WSL2 IP（如 `172.28.123.45`），说明解析成功 ✅  
如果提示“找不到主机”，说明你还没改 hosts 或拼写错误 ❌

---

### ⚠️ 注意事项

1. **必须用 `.localhost`，不能是 `.local`、`.test` 等**
   - `.local` 会被 mDNS（Bonjour/Zeroconf）接管，可能不稳定；
   - `.test` 虽也是保留域名，但部分企业 VPN 仍可能劫持；
   - **只有 `.localhost` 是 100% 强制本地解析的**。

2. **不要用 `localhost` 本身**
   - `localhost` 默认指向 `127.0.0.1`（Windows 自己），而不是 WSL2；
   - 所以要用 **子域名**，如 `app.localhost`、`api.localhost`。

3. **确保 WSL2 服务监听 `0.0.0.0`**
   例如 Nginx 配置：
   ```nginx
   server {
       listen 80;
       server_name app.localhost;  # 可选
       ...
   }
   ```
   或 Node.js：
   ```js
   app.listen(3000, '0.0.0.0', () => { ... })
   ```

---

## ✅ 总结

### 问题
- 在 WSL2 中运行的 Web 服务，通过 Windows 的 `hosts` 文件绑定域名（如 `dev.wsl.net -> 172.x.x.x`）访问。
- 开启全流量接管型 VPN 后，Windows 无法解析该域名，导致页面打不开。

### 导致问题的原因
- 开启 VPN 后，Windows 的 DNS 请求被强制走远程服务器，忽略本地 `hosts` 文件，导致域名解析失败。

### 解决方案
- 使用 `.localhost` 域名代替 `.local` 或其他自定义域名。
  - 修改 Windows 的 `hosts` 文件，将 `dev.wsl.net` 改为 `wsl.localhost`。
  - 在浏览器中访问 `http://wsl.localhost`。

### 总结
| 问题 | 解决方法 |
|------|----------|
| 开启 VPN 后 `dev.wsl.net` 无法访问 | **改为 `wsl.localhost` 或 `dev.wsl.localhost`** |
| 原因 | VPN 劫持 DNS，绕过本地 `hosts` |
| 为什么 `.localhost` 有效 | RFC 强制本地解析，不走 DNS |
| 是否需要重启 WSL？ | ❌ 不需要 |
| 是否需要改代码？ | ❌ 只需改 hosts 和浏览器地址栏 |

---

> 💡 **一句话终极答案**：  
> **把你的开发域名从 `xxx.local` 改成 `xxx.localhost`，并在 Windows hosts 中绑定 WSL2 IP，即可在开 VPN 时正常访问。**

这是目前最简单、最可靠、兼容性最好的方案，已被无数开发者验证 ✅

试试看吧！如果有任何问题，欢迎继续交流 😊