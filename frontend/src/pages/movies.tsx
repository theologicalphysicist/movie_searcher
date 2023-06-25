import MovieCard from "@/components/MovieCard";
import { Sample } from "@/utils/data";

export default function MoviesPage() {

    return (
        <main className={`flex min-h-screen itens-center justify-between flex-col p-24`}>
            <p>
                Hello There
            </p>
            <MovieCard movie={Sample[0]} ></MovieCard>
        </main>
    );
};