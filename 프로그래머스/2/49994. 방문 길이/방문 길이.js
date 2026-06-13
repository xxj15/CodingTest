const solution = (dirs) => {
  const move = (x, y, dir) => {
    if (dir == "U") {
      [nx, ny] = [x, y + 1];
    } else if (dir == "L") {
      [nx, ny] = [x - 1, y];
    } else if (dir == "R") {
      [nx, ny] = [x + 1, y];
    } else {
      [nx, ny] = [x, y - 1];
    }
    return [nx, ny];
  };

  let x = 0,
    y = 0;
  const ans = new Set();

  for (let d of dirs) {
    const [nx, ny] = move(x, y, d);
    if (nx >= -5 && nx <= 5 && ny >= -5 && ny <= 5) {
      ans.add(`${x}${y}${nx}${ny}`);
      ans.add(`${nx}${ny}${x}${y}`);
      [x, y] = [nx, ny];
    }
  }

  return ans.size / 2;
};
