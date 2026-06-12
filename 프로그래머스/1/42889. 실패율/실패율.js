// 실패율

const solution = (N, stages) => {
  const challenger = new Array(N + 2).fill(0);
  for (const stage of stages) {
    challenger[stage] += 1;
  }

  let tot = stages.length;

  const fail = {};

  for (let i = 1; i <= N; i++) {
    if (challenger[i] == 0) {
      fail[i] = 0;
      continue;
    }
    fail[i] = challenger[i] / tot;
    tot -= challenger[i];
  }

  const result = Object.entries(fail)
    .sort((a, b) => b[1] - a[1])
    .map((v) => Number(v[0]));

  return result;
};
console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));
console.log(solution(4, [4, 4, 4, 4, 4]));
