document.addEventListener("DOMContentLoaded", function() {
    const treeData = {
        name: "Start",
        branches: [
            {
                name: "Yes",
                probability: 0.8,
                branches: [
                    { name: "Yes", probability: 0.6, payoff: 100 },
                    { name: "No", probability: 0.4, payoff: -200 }
                ]
            },
            {
                name: "No",
                probability: 0.2,
                payoff: -100
            }
        ]
    };

    function createTree(node, container) {
        const branch = document.createElement("div");
        branch.className = "branch";

        const nameLabel = document.createElement("span");
        nameLabel.textContent = node.name;
        branch.appendChild(nameLabel);

        if (node.branches) {
            const probabilityInput = document.createElement("input");
            probabilityInput.type = "number";
            probabilityInput.value = node.probability * 100;
            probabilityInput.className = "input-group";
            probabilityInput.addEventListener("input", () => {
                node.probability = probabilityInput.value / 100;
                updateTree();
            });
            branch.appendChild(document.createTextNode(" Probability (%): "));
            branch.appendChild(probabilityInput);
        }

        const payoffInput = document.createElement("input");
        payoffInput.type = "number";
        payoffInput.value = node.payoff || 0;
        payoffInput.className = "input-group";
        payoffInput.addEventListener("input", () => {
            node.payoff = +payoffInput.value;
            updateTree();
        });
        branch.appendChild(document.createTextNode(" Payoff: "));
        branch.appendChild(payoffInput);

        container.appendChild(branch);

        if (node.branches) {
            node.branches.forEach(childNode => {
                const childContainer = document.createElement("div");
                childContainer.className = "leaf";
                branch.appendChild(childContainer);
                createTree(childNode, childContainer);
            });
        }
    }

    function calculateExpectedPayoff(node) {
        if (!node.branches) return node.payoff;

        return node.branches.reduce((sum, branch) => {
            return sum + branch.probability * calculateExpectedPayoff(branch);
        }, 0);
    }

    function updateTree() {
        const treeContainer = document.getElementById("tree-container");
        treeContainer.innerHTML = "";
        createTree(treeData, treeContainer);

        const expectedPayoff = calculateExpectedPayoff(treeData);
        const resultDiv = document.createElement("div");
        resultDiv.textContent = `Expected Payoff: ${expectedPayoff.toFixed(2)}`;
        treeContainer.appendChild(resultDiv);
    }

    updateTree();
});
