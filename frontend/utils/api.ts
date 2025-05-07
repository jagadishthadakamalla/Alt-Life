
export const generateAltLife = async (prompt: string) : Promise<string> => {
    const response = await fetch("http://127.0.0.1:8000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt }),
    });
  
    const data = await response.json();
    console.log("Backend full response :", data);
    if (data.result) {
    return data.result;
    } else {
      throw new Error(data.error || "Failed to generate story");
    }
  }; 