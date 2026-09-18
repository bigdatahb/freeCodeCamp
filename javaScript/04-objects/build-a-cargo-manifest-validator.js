function normalizeUnits(manifest) {
	// 拷贝对象
  const {...result} = manifest;
  if (result.unit === "lb") {
    result.weight = result.weight * 0.45;
    result.unit = "kg";
  }
  return result;
}

function validateManifest(manifest) {
  const obj = {};
  
  if (Object.hasOwn(manifest, "containerId")) {
    const id = manifest.containerId;
	  // 检查 id 是否是正整数
    if (!(Number.isInteger(id) && id > 0)) {
      obj.containerId = "Invalid";
    }
  } else {
    obj.containerId = "Missing";
  }

  if (Object.hasOwn(manifest, "destination")) {
    const destination = manifest.destination;
	  // 检查 destination 是否是空字符串
    if (typeof destination !== "string" || destination.trim() === "") {
      obj.destination = "Invalid";
    }
  } else {
    obj.destination = "Missing";
  }

  if (Object.hasOwn(manifest, "weight")) {
    const weight = manifest.weight;
	  // 检查 weight 是否是正数
    if(typeof weight !== "number" || Number.isNaN(weight) || weight <= 0) {
      obj.weight = "Invalid";
    }
  }else {
    obj.weight = "Missing";
  }

  if (Object.hasOwn(manifest, "unit")) {
    const unit = manifest.unit;
	  // 检查 unit 是否是 "kg" 或者 "lb"
    if (typeof unit !== "string" || (unit !== "kg" && unit !== "lb")) {
      obj.unit = "Invalid";
    }
  } else {
    obj.unit = "Missing";
  }

  if (Object.hasOwn(manifest, "hazmat")) {
    const hazmat = manifest.hazmat;
	  // 检查 hazmat 是否是布尔值
    if (typeof hazmat !== "boolean") {
      obj.hazmat = "Invalid";
    }
  } else {
    obj.hazmat = "Missing";
  }
  return obj;
}

function processManifest(manifest) {
  const result = validateManifest(manifest);
  const containerId = manifest.containerId;
  if (Object.keys(result).length === 0) {
    // valid
    const normalizedObj = normalizeUnits(manifest);
    const weight = normalizedObj.weight;
    console.log(`Validation success: ${containerId}`);
    console.log(`Total weight: ${weight} kg`)
  } else {
    console.log(`Validation error: ${containerId}`)
    console.log(result);
  }
}
