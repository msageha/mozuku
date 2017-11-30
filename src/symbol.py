
special_char_dict = {'㌃': 'アール', '…': 'テン', '∩': 'キゴウ', '〓': 'キゴウ', '＝': 'ケイサン', '∫': 'キゴウ', '↑': 'ヤジルシ', '¥': 'エン', '￥': 'エン',
      '∪': 'キゴウ', '♂': 'キゴウ', '〃': 'ドウ', '仝': 'キゴウ', 'ゞ': 'キゴウ', 'ゝ': 'キゴウ', 'ヾ': 'キゴウ', 'ヽ': 'キゴウ', '々': 'ドウ', '♪': 'キゴウ',
      '∠': 'キゴウ', '×': 'バツ', '【': 'カッコヒラキ', '】': 'カッコトジ', '『': 'カッコヒラキ', '』': 'カッコトジ', '《': 'カッコヒラキ', '》': 'カッコトジ',
      '「': 'カッコヒラキ', '」': 'カッコトジ', '〈': 'カッコヒラキ', '〉': 'カッコトジ', '｛': 'カッコヒラキ', '｝': 'カッコトジ', '［': 'カッコヒラキ', '］': 'カッコトジ',
      '（': 'カッコヒラキ', '）': 'カッコトジ', '≪': 'キゴウ', '≫': 'キゴウ', '｢': 'カッコヒラキ', '｣': 'カッコトジ', '{': 'カッコヒラキ', '}': 'カッコトジ',
      '[': 'カッコヒラキ', ']': 'カッコトジ', '<': 'カッコヒラキ', '>': 'カッコトジ', '(': 'カッコヒラキ', ')': 'カッコトジ', '〔': 'カッコヒラキ', '〕': 'カッコトジ',
      '㈱': 'カブシキガイシャ', '㏍': 'カブシキガイシャ', '～': 'ヨリ', '㌍': 'カロリー', '，': 'テン', '〆': 'シメ', '―': 'キゴウ', '‐': 'キゴウ', '“': 'キゴウ',
      '"': 'キゴウ', '／': 'シャセン', '/': 'シャセン', '〇': 'マル', '＿': 'キゴウ', '￣': 'キゴウ', '¨': 'テン', '｀': 'テン', '´': 'テン', '゜': 'ハンダクテン', '゛': 'テン',
      '＼': 'シャセン', '\\': 'シャセン', '§': 'セクション', '＾': 'キゴウ', '￢': 'キゴウ', '⇒': 'キゴウ', '⇔': 'キゴウ', '∀': 'キゴウ', '∃': 'キゴウ', '⊥': 'スイチョク',
      '⌒': 'キゴウ', '∂': 'キゴウ', '∇': 'キゴウ', '≡': 'ゴウドウ', '∨': 'キゴウ', '†': 'ダガー', '√': 'ルート', '∽': 'キゴウ', '∝': 'キゴウ', '∵': 'ナゼナラバ', '∬': 'キゴウ',
      'Å': 'タンイ', '‰': 'タンイ', '♯': 'シャープ', '♭': 'フラット', '‡': 'キゴウ', '′': 'フン', '≒': 'キンジ', '∥': 'タテボウ', '∧': 'キゴウ', '｜': 'タテボウ',
      '±': 'プラスマイナス', '÷': 'ワル', '≠': 'フトウゴウ', '≦': 'フトウゴウ', '≧': 'フトウゴウ', '∞': 'ムゲンダイ', '∴': 'ユエニ', '♀': 'メス', '‥': 'キゴウ',
      '°': 'ド', '⊃': 'キゴウ', '⊂': 'キゴウ', '⊇': 'キゴウ', '⊆': 'キゴウ', '∋': 'キゴウ', '∈': 'キゴウ', '〒': 'ユウビンバンゴウ', '※': 'ホシ', '″': 'ビョウ',
      '㌔': 'キロ', '㎏': 'キログラム', '㎞': 'キロメートル', '㌘': 'グラム', '★': 'ホシ', '●': 'ズケイ', '㊦': 'シタ', '－': 'マイナス', '＋': 'プラス',
      '＜': 'ダイナリ', '＞': 'ショウナリ', '▲': 'ズケイ', '▽': 'ズケイ', '△': 'ズケイ', '▼': 'ズケイ', '⊿': 'サンカクケイ', 'cc': 'シーシー', '◇': 'ヒシ',
      '◆': 'ヒシ', '□': 'ズケイ', '■': 'ズケイ', '↓': 'ヤジルシ', '㍼': 'ショウワ', '㊤': 'ジョウ', '☆': 'ホシ', '○': 'マル', '◎': 'マル', '℃': 'ド', '㎝': 'センチメートル',
      '㌢': 'センチ', '￠㌣': 'セント', '㍽': 'タイショウ', '㈹': 'ダイヒョウ', '￠': 'タンイ', '￡': 'タンイ', '％': 'パーセント', '＄': 'タンイ', '㊥': 'チュウ',
      '∟': 'チョッカク', '；': 'テン', '：': 'テン', '．': 'マル', '、': 'テン', '.': 'テン', '・': 'テン', '･': 'テン', ':': 'テン', ';': 'テン', 'ﾞ': 'テン',
      'ﾟ': 'テン', '℡': 'デンワ', '㌧': 'トン', '№': 'ナンバー', '%': 'パーセント', '㌫': 'パーセント', '㊧': 'ヒダリ', '←': 'ヤジルシ', '∮': 'ファイ', '㍻': 'ヘイセイ',
      '㎡': 'ヘイホウメートル', '㌶': 'ヘクタール', '㌻': 'ペイジ', '｡': 'マル', '。●': 'マル', '→': 'ヤジルシ', '㊨': 'ミギ', '㎜': 'ミリメートル', '㍉': 'ミリ',
      '㎎': 'ミリグラム', '㍊': 'ミリバール', '㍍': 'メートル', '㍾': 'メイジ', '㈲': 'ユウゲンガイシャ', '㍑': 'リットル', '㍗': 'ワット' }