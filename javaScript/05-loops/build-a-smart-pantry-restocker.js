const pantry = [
  { sku: "A10", name: "Tomatoes", qty: 4, expires: "2027-01-01", zone: "fridge" },
  { sku: "D43", name: "Pineapples", qty: 2, expires: "2020-01-01", zone: "general" }
];

const rawData = [
  "A10|Tomatoes|5|2027-01-01",
  "B21|Bananas|10|2027-01-01",
  "C32|Eggs|3|2027-01-01|fridge",
  "C32|Eggs|3|2027-01-01",
  "D43|Pineapples|0|2027-01-01",
  "E54|Peppers|-1|2027-01-01|fridge"
];

function parseShipment(rawData) {
  const result = [];
  for(const item of rawData) {
    const data = item.split("|");
    const sku = data[0];
    if(exists(result, sku)) {
      continue;
    }
    const name = data[1];
    const qty = Number.parseInt(data[2]);
    const expires = data[3];
    let zone = "general";
    if(data.length === 5) {
      zone = data[4];
    }
    result.push({sku, name, qty, expires, zone});
  }
  return result;
}

function exists(pantry, sku) {
  for(const product of pantry) {
    if(product.sku === sku) {
      return true;
    }
  }
  return false;
}

function planRestock(pantry, shipment) {
  const result = [];
  for(let i = 0; i < shipment.length; ++i) {
    const s = shipment[i];
    const action = {};
    if(s.qty <= 0) {
      action.type = "discard";
    } else if (exists(pantry, s.sku)) {
      action.type = "restock";
    } else {
      action.type = "donate";
    }
    action.item = s;
    result.push(action);
  }
  return result;
}

function groupByZone(actions) {
  const result = {};
  for(const action of actions) {
    const zone = action.item.zone;
    if(Object.hasOwn(result, zone)) {
      result[zone].push(action);
    } else {
      result[zone] = [];
      result[zone].push(action);
    }
  }
  return result;
}

function clonePantry(pantry) {
  // deep copy
  const json = JSON.stringify(pantry);
  return JSON.parse(json);
}

const shipment = parseShipment(rawData);
const actions = planRestock(pantry, shipment);
console.log(groupByZone(actions));
