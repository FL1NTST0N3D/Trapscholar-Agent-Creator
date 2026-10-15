import React, { useState } from "react";
export default function App() {
  const [plants, setPlants] = useState([]);
  const [name, setName] = useState("");

  return (
    <div style={{padding:20}}>
      <input value={name} onChange={e=>setName(e.target.value)} placeholder="Plant Name"/>
      <button onClick={()=>{setPlants([...plants,{name}]); setName("");}}>Add</button>
      {plants.map((p,i)=><div key={i}>{p.name}</div>)}
    </div>
  );
}