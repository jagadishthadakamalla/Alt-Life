import { useState } from "react";
import { generateAltLife } from "../utils/api";

export default function GenerateAltLifeStory() {
  const [prompt, setPrompt] = useState("");
  const [story, setStory] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    console.log("Prompt Submitted:", prompt); // Debugging line
    try {
      const result = await generateAltLife(prompt);
      console.log("Result from backend:", result); // Debugging line
      setStory(result);
    } catch (error) {
      console.error("Error calling API:", error); // Debugging line
      setStory("An error occurred while generating your story. Please try again.");
    }
    setLoading(false);
  };

  return (
    <div className="max-w-xl mx-auto mt-10">
      {/* Example Prompt Section */}
      <div className="mb-4 bg-gray-100 p-4 rounded">
        <h3 className="font-semibold text-lg">Example Prompt</h3>
        <p className="text-gray-600">
          Here's an example of what you can write to get started:
        </p>
        <p className="mt-2 italic">"I became a software engineer, but I always dreamed of writing novels."</p>
      </div>

      {/* Form Section */}
      <form onSubmit={handleSubmit} className="space-y-4">
        <textarea
          className="w-full border rounded p-3"
          rows={4}
          placeholder="Describe your alternate life dream..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
        <button
          className="bg-blue-600 text-white px-4 py-2 rounded"
          type="submit"
        >
          {loading ? "Creating..." : "Generate Alt-Life"}
        </button>
      </form>

      {/* Display Generated Story */}
      {story && (
        <div className="mt-6 bg-gray-100 p-4 rounded">
          <h2 className="font-bold mb-2">Your Alt-Life Story:</h2>
          <p>{story}</p>
        </div>
      )}
    </div>
  );
}
