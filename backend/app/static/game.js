const grid = document.getElementById("grid");
const scoreDisplay = document.getElementById("score");

let board = [];
let score = 0;

function initBoard() {
    board = Array(4)
        .fill()
        .map(() => Array(4).fill(0));

    score = 0;

    addRandomTile();
    addRandomTile();

    renderBoard();
}

function addRandomTile() {
    const empty = [];

    for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
            if (board[r][c] === 0) {
                empty.push([r, c]);
            }
        }
    }

    if (!empty.length) return;

    const [r, c] = empty[Math.floor(Math.random() * empty.length)];

    board[r][c] = Math.random() > 0.1 ? 2 : 4;
}

function renderBoard() {
    grid.innerHTML = "";

    board.flat().forEach((value) => {
        const cell = document.createElement("div");

        cell.className = "cell";
        cell.dataset.value = value;

        cell.textContent = value || "";

        grid.appendChild(cell);
    });

    scoreDisplay.textContent = `Score: ${score}`;
}

function slide(row) {
    row = row.filter((v) => v);

    for (let i = 0; i < row.length - 1; i++) {
        if (row[i] === row[i + 1]) {
            row[i] *= 2;
            score += row[i];
            row[i + 1] = 0;
        }
    }

    row = row.filter((v) => v);

    while (row.length < 4) {
        row.push(0);
    }

    return row;
}

function rotateBoard() {
    const newBoard = Array(4)
        .fill()
        .map(() => Array(4).fill(0));

    for (let r = 0; r < 4; r++) {
        for (let c = 0; c < 4; c++) {
            newBoard[c][3 - r] = board[r][c];
        }
    }

    board = newBoard;
}

function moveLeft() {
    let changed = false;

    for (let r = 0; r < 4; r++) {
        const original = [...board[r]];
        board[r] = slide(board[r]);

        if (JSON.stringify(original) !== JSON.stringify(board[r])) {
            changed = true;
        }
    }

    return changed;
}

function move(direction) {
    let rotated = 0;

    if (direction === "up") rotated = 3;
    if (direction === "right") rotated = 2;
    if (direction === "down") rotated = 1;

    for (let i = 0; i < rotated; i++) {
        rotateBoard();
    }

    const changed = moveLeft();

    for (let i = 0; i < (4 - rotated) % 4; i++) {
        rotateBoard();
    }

    if (changed) {
        addRandomTile();
        renderBoard();
    }
}

document.addEventListener("keydown", (e) => {
    switch (e.key) {
        case "ArrowLeft":
            move("left");
            break;

        case "ArrowRight":
            move("right");
            break;

        case "ArrowUp":
            move("up");
            break;

        case "ArrowDown":
            move("down");
            break;
    }
});

function restartGame() {
    initBoard();
}

initBoard();