const equipmentLedger = {
  "1": { type: "PC", status: "CheckedOut", borrower: { name: "John Smith", email: "john@acme.org" }, dueDate: "11/30/2025" },
  "2": { type: "Laptop", status: "CheckedIn", borrower: { name: "", email: "" }, dueDate: "" },
  "3": { type: "Laptop", status: "CheckedOut", borrower: { name: "Jane Doe", email: "jane@acme.org" }, dueDate: "10/31/2025" },
  "4": { type: "iPad", status: "CheckedIn", borrower: { name: "", email: "" }, dueDate: "" }
};

function checkoutDevice(ledger, assetTag, borrower) {
  
  if (!Object.hasOwn(ledger, assetTag)) {
    const msg = `${assetTag} not found.`;
    return {ledger: ledger, message: msg};
  }

  if (ledger[assetTag].status === "CheckedOut") {
    const msg = `${assetTag} already checked out.`;
    
    return {ledger: ledger, message: msg};
  }

  // deep clone
  const jsonStr = JSON.stringify(ledger);
  const copy = JSON.parse(jsonStr);

  copy[assetTag].status = "CheckedOut";
  copy[assetTag].borrower.name = borrower.name;
  copy[assetTag].borrower.email = borrower.email;
  
  return {ledger: copy, message: `${assetTag} ${borrower.name}`}; 
}

function checkinDevice(ledger, assetTag) {
  if(!Object.hasOwn(ledger, assetTag)) {
    const msg = `${assetTag} not found.`;
    return {ledger: ledger, message: msg};
  }

  // deep clone
  const jsonStr = JSON.stringify(ledger);
  const copy = JSON.parse(jsonStr);

  copy[assetTag].borrower.name = "";
  copy[assetTag].borrower.email = "";
  copy[assetTag].dueDate = "";
  copy[assetTag].status = "CheckedIn";
  return {ledger: copy, message: `${assetTag} checked in`};
}

function standardDate(dateStr) {
  if (dateStr === "") return "00000000";
  const [month, day, year] = dateStr.split("/");
  return `${year}${month.padStart(2, '0')}${day.padStart(2, '0')}`;
}

function listOverdueDevices(ledger, today) {
  const result = [];
  for(const tag of Object.keys(ledger)) {
    const obj = ledger[tag];
    if (obj.status !== "CheckedOut") {
      continue;
    }
    const dueDate = standardDate(obj.dueDate);
    const td = standardDate(today);
    if (dueDate < td) {
      result.push(obj);
    }
  }
  return result.sort((a, b) => {
    return standardDate(a.dueDate) - standardDate(b.dueDate);
  });
}

function serializeLedger(ledger) {
  return JSON.stringify(ledger);
}

function loadLedger(json) {
  return JSON.parse(json);
}

