const questions = [
  {
    category: "历史",
    question: "918事变发生在哪一年?",
    choices: ["1930", "1931", "1932"],
    answer: "1931"
  },
  {
    category: "历史",
    question: "中华人民共和国成立于哪一年?",
    choices: ["1945", "1949", "1976"],
    answer: "1949"
  },
  {
    category: "文化",
    question: "林黛玉葬花是在哪一个节气?",
    choices: ["惊蛰", "处暑", "芒种"],
    answer: "芒种"
  },
  {
    category: "文化",
    question: "下面哪一个乐器时代最早?",
    choices: ["骨笛", "陶埙", "古琴"],
    answer: "骨笛"
  },
  {
    category: "信息技术",
    question: "下面哪一个是正确的IP地址?",
    choices: ["268.12.3.4", "192.23.2", "194.10.0.22"],
    answer: "194.10.0.22"
  }
];

function getRandomQuestion(questions) {
  return questions[Math.floor(Math.random() * questions.length)];
}

function getRandomComputerChoice(choices) {
  return choices[Math.floor(Math.random() * choices.length)];
}


function getResults(question, choice) {
  if (question.answer === choice) {
    return "The computer's choice is correct!";
  }
  return `The computer's choice is wrong. The correct answer is: ${question.answer}`;
}
