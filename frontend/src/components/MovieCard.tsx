import React, {JSX} from "react"

import { Movie } from "@/utils/types";


const MovieCard = (props: {movie: Movie}): JSX.Element => {

    return (
        <div className="bg-white p-4">
            <header className="text-black">
                <h1 className="text-xl font-bold">{props.movie.title}</h1>
            </header>
        </div>
    );
};

export default MovieCard;