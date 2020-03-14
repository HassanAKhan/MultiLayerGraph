
var mpnet = JSON.parse('{{ file_data }}');
console.log(mpnet);
var color = d3.scale.category20();
var svg_layer = [];
var node_layer = [];
var link_layer = [];
var layer_label = [];
var intra_svg = []
var intra_link = [];


var width = Math.sqrt(mpnet.nodes.length) * 150;
var height = 4 / 6 * width;
var fontsize = Math.max(width * 0.05, 16)



var force = d3.layout.force()
    .charge(-30)
    .linkDistance(100)
    .size([width, height])
    .nodes(mpnet.nodes)
    .links(mpnet.links)
    .start();


var nlayers = mpnet.layers.length;
for (var layer = nlayers - 1; layer >= 0; layer--) {
    svg_layer[layer] = d3.select("body").append("svg")
        .attr("layer", 0)
        .style("position", "absolute")
        .style("left", "100px")
        .style("top", (width / 6 + layer * width / 4).toString() + "px")
        .style("background-color", "rgba(100,100,100,0.3)")
        .style("transform", "rotate3D(-0.9,0.4,0.4,70deg)") // Firefox
        .style("-webkit-transform", "rotate3D(-0.9,0.4,0.4,70deg)") // Safari, Chrome
        .attr("width", width)
        .attr("height", height);




    layer_label[layer] = svg_layer[layer].selectAll(".layerlabel")
        .data([mpnet.layers[layer]])
        .enter()
        .append("text")
        .text((d) => d.name)
        .attr("dx", function (d) { return width - 0.8 * d.name.toString().length * fontsize; })
        .attr("dy", fontsize)
        .style("font-size", fontsize + "px")
        .style("fontcolor", "black")

    link_layer[layer] = svg_layer[layer].selectAll(".link")
        .data(mpnet.links)
        .enter()
        .append("line")
        .filter(function (d) {

            if (d.layer == layer) {
                return d.layer === layer
            }
        })

        .style("stroke-width", function (d) { return 2 * Math.sqrt(d.value); })
        .style("stroke", "#999");

    node_layer[layer] = svg_layer[layer].selectAll(".node")
        .data(mpnet.nodes)
        .enter()
        .append("circle")
        .filter(function (d) { return d.layer === layer })
        .attr("class", "node")
        .attr("r", 5)
        .style("fill", function (d) { return color(d.index); })
        .style("stroke", "#fff")
        .style("stroke-width", "1.5px")
        .call(force.drag);

    node_layer[layer].append("title")
        .text(function (d) { return d.name; });


}





force.on("tick", function () {

    for (var layer = 0; layer < nlayers; layer++) {
        link_layer[layer].attr("x1", function (d) { return d.source.x; })
            .attr("y1", function (d) { return d.source.y; })
            .attr("x2", function (d) { return d.target.x; })
            .attr("y2", function (d) { return d.target.y; });


        node_layer[layer].attr("cx", function (d) { return d.x; })
            .attr("cy", function (d) { return d.y; });



    };

    var nelm = intra_link.length;
    for (elm in intra_link) {

        intra_link[elm].attr("x1", mpnet.links[elm].source.x)
            .attr("y1", mpnet.links[elm].source.y)
            .attr("x2", mpnet.links[elm].target.x)
            .attr("y2", mpnet.links[elm].target.y);
    };
});