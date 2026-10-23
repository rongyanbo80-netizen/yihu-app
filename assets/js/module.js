/* module.js —— 模块详情页渲染 */
(function () {
  const params = new URLSearchParams(location.search);
  const id = params.get('id');
  const index = MODULES.findIndex(function (m) { return m.id === id; });

  if (index < 0) {
    location.replace('index.html');
    return;
  }

  const m = MODULES[index];
  document.title = m.name + ' · 颐护小护';

  // 顶栏直接显示模块名，正文标题同步填充（不出现“加载中”）
  const barTitle = document.getElementById('bar-title');
  if (barTitle) barTitle.textContent = m.name;

  const art = document.getElementById('art');
  const img = document.createElement('img');
  img.src = 'assets/img/hero-' + m.id + '.svg';
  img.alt = m.name + ' 示意图';
  art.appendChild(img);

  const badge = document.getElementById('badge');
  badge.style.background = m.tint;
  const bi = document.createElement('img');
  bi.src = 'assets/img/icon-' + m.id + '.svg';
  bi.alt = '';
  bi.width = 28;
  bi.height = 28;
  badge.appendChild(bi);

  document.getElementById('title').textContent = m.name;
  document.getElementById('lead').textContent = m.lead;
  document.getElementById('problem').textContent = m.problem;

  /* ---- 怎么工作 ---- */
  const steps = document.getElementById('steps');
  m.steps.forEach(function (s) {
    const li = document.createElement('li');
    li.innerHTML = '<strong>' + s.t + '</strong><span>' + s.d + '</span>';
    steps.appendChild(li);
  });

  /* ---- 流程示意图（四步主流程） ---- */
  function buildFlow(steps, accent) {
    const xs = [95, 275, 455, 635];
    let svg =
      '<svg viewBox="0 0 730 190" role="img" aria-label="工作流程示意">' +
      '<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">' +
      '<path d="M0,0 L6,3 L0,6 Z" fill="#b9d2c9"/></marker></defs>' +
      '<rect x="16" y="12" width="698" height="166" rx="18" fill="#fbfdfc" stroke="' + accent +
      '" stroke-opacity=".35" stroke-dasharray="6 6"/>';

    for (let i = 0; i < 3; i++) {
      svg += '<line x1="' + (xs[i] + 30) + '" y1="75" x2="' + (xs[i + 1] - 32) +
        '" y2="75" stroke="#b9d2c9" stroke-width="2" marker-end="url(#ah)"/>';
    }

    steps.forEach(function (s, i) {
      const x = xs[i];
      svg +=
        '<circle cx="' + x + '" cy="75" r="26" fill="#fff" stroke="' + accent + '" stroke-width="2"/>' +
        '<text x="' + x + '" y="81" text-anchor="middle" font-size="17" font-weight="700" fill="' +
        accent + '">' + (i + 1) + '</text>' +
        '<text x="' + x + '" y="128" text-anchor="middle" font-size="15" fill="#17251f">' +
        s.t + '</text>' +
        '<text x="' + x + '" y="150" text-anchor="middle" font-size="11.5" fill="#8b9a94">STEP ' +
        (i + 1) + '</text>';
    });

    return svg + '</svg>';
  }

  const flow = document.getElementById('flow');
  if (flow) flow.innerHTML = buildFlow(m.steps, m.accent);

  /* ---- 分支判断 ---- */
  const branch = document.getElementById('branch');
  if (branch && m.branch) {
    branch.innerHTML =
      '<div class="branch-title">判断点 · ' + m.branch.at + '</div>' +
      '<div class="branch-item ok"><span class="b-tag">是</span><span>' + m.branch.ok + '</span></div>' +
      '<div class="branch-item no"><span class="b-tag">否</span><span>' + m.branch.no + '</span></div>';
  }

  /* ---- 参数条形图 ---- */
  const bars = document.getElementById('bars');
  if (bars && m.bars) {
    m.bars.forEach(function (b) {
      const row = document.createElement('div');
      row.className = 'bar-row';
      row.innerHTML =
        '<span class="bar-label">' + b.label + '</span>' +
        '<span class="bar-track"><i class="bar-fill" style="width:' + b.pct +
        '%;background:linear-gradient(90deg,' + m.accent + '55,' + m.accent + ')"></i></span>' +
        '<span class="bar-value">' + b.text + '</span>';
      bars.appendChild(row);
    });
  }

  /* ---- 参数表 ---- */
  const specs = document.getElementById('specs');
  m.specs.forEach(function (row) {
    const tr = document.createElement('tr');
    tr.innerHTML = '<td>' + row[0] + '</td><td>' + row[1] + '</td>';
    specs.appendChild(tr);
  });

  /* ---- 场景 ---- */
  const chips = document.getElementById('chips');
  m.scenes.forEach(function (s) {
    const span = document.createElement('span');
    span.className = 'chip';
    span.textContent = s;
    chips.appendChild(span);
  });

  /* ---- 上一个 / 下一个 ---- */
  const pager = document.getElementById('pager');
  const prev = MODULES[(index - 1 + MODULES.length) % MODULES.length];
  const next = MODULES[(index + 1) % MODULES.length];
  pager.innerHTML =
    '<a href="module.html?id=' + prev.id + '">← 上一个<strong>' + prev.name + '</strong></a>' +
    '<a href="module.html?id=' + next.id + '" style="text-align:right">下一个 →<strong>' + next.name + '</strong></a>';
})();
