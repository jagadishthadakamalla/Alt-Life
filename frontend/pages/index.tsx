import Head from "next/head";
import AltLifeForm from "../components/AltLifeForm";

export default function Home() {
  return (
    <>
      <Head>
        <title>Alt-Life | Gen Z Simulator</title>
      </Head>
      <main className="min-h-screen bg-white p-6">
        <h1 className="text-3xl font-bold text-center mb-6">
          Alt-Life: Dream It. Live It.
        </h1>
        <AltLifeForm />
      </main>
    </>
  );
}