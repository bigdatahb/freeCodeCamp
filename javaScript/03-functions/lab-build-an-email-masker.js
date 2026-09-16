// 将邮箱地址用户名部分信息进行脱敏，比如 test@example.com 变成 t**t@example.com
function maskEmail(email) {
  const index = email.indexOf('@');
  // 先获取需要脱敏的部分子串
  const target = email.slice(1, index - 1);
  // 然后将目标子串替换为相同字符数目的 *
  return email.replace(target, '*'.repeat(target.length));
}

const email = 'apple.pie@example.com';
console.log(maskEmail(email));
