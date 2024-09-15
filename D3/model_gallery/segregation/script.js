const width = 480;
const height = 480;
const size = 32;
const cellSize = width / size;

let grid = [];
const red = '#FFD700';
const blue = '#4B0082';

const svg = d3.select("#visualization")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

function initializeGrid() {
    grid = [];
    for (let i = 0; i < size; i++) {
        grid[i] = [];
        for (let j = 0; j < size; j++) {
            grid[i][j] = Math.random() < 0.5 ? red : blue;
        }
    }
    drawGrid();
    updateIndices();
}

function drawGrid() {
    svg.selectAll("rect")
        .data(grid.flat())
        .join("rect")
        .attr("x", (d, i) => (i % size) * cellSize)
        .attr("y", (d, i) => Math.floor(i / size) * cellSize)
        .attr("width", cellSize)
        .attr("height", cellSize)
        .attr("fill", d => d)
        .attr("class", "cell");
}

function countNeighbors(x, y, color) {
    let count = 0;
    let total = 0;
    for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
            if (i === 0 && j === 0) continue;
            const nx = (x + i + size) % size;
            const ny = (y + j + size) % size;
            total++;
            if (grid[nx][ny] === color) {
                count++;
            }
        }
    }
    return total === 0 ? 0 : count / total;
}

function moveAgent(x, y) {
    const color = grid[x][y];
    let foundNewLocation = false;
    for (let i = 0; i < size && !foundNewLocation; i++) {
        for (let j = 0; j < size && !foundNewLocation; j++) {
            if (grid[i][j] === color) continue;
            const neighborRatio = countNeighbors(i, j, color);
            const threshold = document.getElementById('threshold').value / 100;
            if (neighborRatio >= threshold) {
                const oldColor = grid[i][j];
                grid[i][j] = color;
                grid[x][y] = oldColor;
                animateMove(x, y, i, j, color, oldColor);
                foundNewLocation = true;
            }
        }
    }
    return foundNewLocation;
}

function animateMove(fromX, fromY, toX, toY, color, oldColor) {
    const fromCell = svg.select(`rect[x="${fromX * cellSize}"][y="${fromY * cellSize}"]`);
    const toCell = svg.select(`rect[x="${toX * cellSize}"][y="${toY * cellSize}"]`);

    fromCell.transition()
        .duration(800)
        .attr("fill", oldColor);

    toCell.transition()
        .duration(500)
        .attr("fill", color);
}

function runModel() {
    const threshold = document.getElementById('threshold').value / 100;
    let moves = 0;
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            const color = grid[i][j];
            const neighborRatio = countNeighbors(i, j, color);
            if (neighborRatio < threshold) {
                if (moveAgent(i, j)) {
                    moves++;
                }
            }
        }
    }
    updateIndices();
    if (moves > 0) {
        setTimeout(runModel, 600);
    }
}

function calculateHappinessIndex() {
    let happyAgents = 0;
    const threshold = document.getElementById('threshold').value / 100;
    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            const color = grid[i][j];
            const neighborRatio = countNeighbors(i, j, color);
            if (neighborRatio >= threshold) {
                happyAgents++;
            }
        }
    }
    return (happyAgents / (size * size)) * 100;
}

// function calculateDissimilarityIndex() {
//     let totalRed = 0;
//     let totalBlue = 0;
//     let dissimilarity = 0;

//     for (let i = 0; i < size; i++) {
//         for (let j = 0; j < size; j++) {
//             if (grid[i][j] === red) {
//                 totalRed++;
//             } else {
//                 totalBlue++;
//             }
//         }
//     }

//     for (let i = 0; i < size; i++) {
//         for (let j = 0; j < size; j++) {
//             const redNeighbors = countNeighbors(i, j, red) * 8;
//             const blueNeighbors = countNeighbors(i, j, blue) * 8;
//             dissimilarity += Math.abs(redNeighbors / totalRed - blueNeighbors / totalBlue);
//         }
//     }

//     return dissimilarity / (2 * size * size);
// }

// function calculateDissimilarityIndex() {
//     let totalRed = 0;
//     let totalBlue = 0;
//     let dissimilarity = 0;

//     // Count total red and blue inhabitants
//     for (let i = 0; i < size; i++) {
//         for (let j = 0; j < size; j++) {
//             if (grid[i][j] === red) {
//                 totalRed++;
//             } else if (grid[i][j] === blue) {
//                 totalBlue++;
//             }
//         }
//     }

//     // Dissimilarity calculation
//     for (let i = 0; i < size; i++) {
//         for (let j = 0; j < size; j++) {
//             const redNeighbors = countNeighbors(i, j, red);
//             const blueNeighbors = countNeighbors(i, j, blue);

//             // Proportional contribution to dissimilarity
//             const totalNeighbors = redNeighbors + blueNeighbors;
//             if (totalNeighbors > 0) {
//                 const proportionRed = redNeighbors / totalNeighbors;
//                 const proportionBlue = blueNeighbors / totalNeighbors;
//                 dissimilarity += Math.abs(proportionRed - (totalRed / (totalRed + totalBlue))) +
//                                  Math.abs(proportionBlue - (totalBlue / (totalRed + totalBlue)));
//             }
//         }
//     }

//     // Normalize dissimilarity index
//     return dissimilarity / (2); // Normalize against the maximum possible dissimilarity (which is 2)
// }

// function updateIndices() {
//     const happinessIndex = calculateHappinessIndex();
//     const dissimilarityIndex = calculateDissimilarityIndex();
//     document.getElementById('happiness-value').textContent = happinessIndex.toFixed(2);
//     document.getElementById('dissimilarity-value').textContent = dissimilarityIndex.toFixed(4);
// }

function resetGrid() {
    initializeGrid();
}

// Initialize the grid when the page loads
window.onload = initializeGrid;