const solution = (arr1, arr2) => {
  const r1 = arr1.length;
  const r2 = arr1[0].length;
  const r3 = arr2[0].length;

  const newArr = [];
  for (let i = 0; i < r1; i++) {
    newArr.push(new Array(r3).fill(0));
  }

  for (let i = 0; i < r1; i++) {
    for (let j = 0; j < r3; j++) {
      for (let k = 0; k < r2; k++) {
        newArr[i][j] += arr1[i][k] * arr2[k][j];
      }
    }
  }
  return newArr;
};
