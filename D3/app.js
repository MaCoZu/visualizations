const canvas = d3.select('.canva');

const width = 600;
const height = 400;
const margin = { top: 30, bottom: 30, left: 30, right: 30 };

// canvas with margins
const svg = canvas
    .append("svg") 
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .style("border", "5px dashed #f46664 ")
    .style("background-color", "#f4ae64")

// chart area with borders
const g = svg
    .append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);

//  add a rectange inside the chart area 
g.append("rect")
    .attr("width", width)
    .attr("height", height)
    .style("fill", "#f2f464");

// // Load external JSON data
// d3.json("data.json").then(function(data) {
//     const rect = g.selectAll("rect")
//         .data(data)
//         .enter().append("rect")
//         .attr("width", (d) => d.width * 3)
//         .attr("fill", (d) => d.fill)
//         .attr("rx", 5)
//         .attr("height", (d) => d.height * 2)
//         .attr("x", (d, i) => i * (d.width * 3) + 10)
//         .attr("y", (d) => height - (d.height * 2));

// }).catch(function(error) {
//     console.error("Error loading the data:", error);
// });


    // rect.attr("width", 24)
    //     .data(dataArray)
    //     .attr("fill", "orange")
    //     .attr("height", function(d){return d*2})  
    //     .attr("x", function(i){return i*25})



// const svg = canvas.append('svg')
//                   .attr('width',800)
//                   .attr('height',250);

// svg.append('rect')
//     .attr('width',400)
//     .attr('height', '50%')
//     .attr('fill', 'blue')
//     .attr('rx', 15)
//     .attr("fill-opacity", "0.4");

// svg.append('circle')
//     .attr('cx', 400)
//     .attr('cy', '60%')
//     .attr('r', 50 )
//     .attr('fill', 'yellow')
//     .style("stroke-width", 5)    // set the stroke width
//     .style("stroke", "red")
//     .style("fill", "none");
                  

// svg.append('line')
//     .attr('x1', 50)
//     .attr('y1', 140)
//     .attr('x2', 300)
//     .attr('y2', 160)
//     .attr('stroke', 'green')
//     .style("stroke-width", 5);

// svg.append("text")
//     .text("Playing")
//     .attr("font-size", 50)
//     .attr("font-weight", "bold")
//     .attr("x", 50)
//     .attr("y", 40)

// svg.append("text")
//     .text("With")
//     .attr("x", 250)
//     .attr("y", 80)
//     .style("font", "italic 70px serif")
//     .style("fill", "brown")
//     .style("stroke", "yellow")
//     ;


// svg.append("text")
//     .text("TEXT")
//     .attr("font-size", 60)
//     .attr("x", 110)
//     .attr("y", 150)
//     .attr("font-stretch", "ultra-expanded")
//     ;
