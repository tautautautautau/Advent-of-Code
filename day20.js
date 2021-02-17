var fs = require("fs");
var iA = fs.readFileSync("input/iA20.txt").toString().split("\r\n\r\n");
let tiles = [];

iA.forEach(tile => {
    let tileRows = tile.split("\r\n");
    let tileObj = {
        ID : +tileRows.splice(0, 1).toString().substr(5, 4),
        grid : tileRows
    }
    tiles.push(tileObj);
});

console.log(tiles[0]);