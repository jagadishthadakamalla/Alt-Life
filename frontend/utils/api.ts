const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL;
export const generateAltLife = async (prompt: string) : Promise<string> => {
    const response = await fetch('${backendUrl}/generate', {
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
