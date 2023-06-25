import * as fs from "fs/promises";
import * as path from "path";
import {parse} from "csv-parse";
import { Stats } from "fs";


export type Genre = 
    "Drama" |
    "Romance" | 
    "Biography" | 
    "Crime" | 
    "History" | 
    "Adventure" | 
    "War" | 
    "Fantasy" | 
    "Mystery" | 
    "Horror" | 
    "Western" | 
    "Comedy" | 
    "Thriller" | 
    "Animation" | 
    "Action" | 
    "Film-Noir" | 
    "Family" | 
    "Sci-Fi" | 
    "Musical"
;

export interface Movie {
    imdb_title_id: string,
    title: string,
    original_title: string,
    year: number,
    date_published: string,
    genre: string,
    duration: number,
    country: string,
    language: string,
    director: string,
    writer: string,
    production_company: string,
    actors: string,
    description: string,
    avg_vote: number,
    votes: number,
    budget: string | null,
    usa_gross_income: string | null,
    worlwide_gross_income: string | null,
    metascore: number | null,
    reviews_from_users: number | null,
    reviews_from_critics: number | null
};

const CSV_PATH = `${process.env.PROJECT_PATH}preprocessing/csv/IMDb movies.csv`;
const TYPES_PATH = `${process.env.PROJECT_PATH}frontend/src/utils/types.ts`;

const CSV_HEADERS = [
    "imdb_title_id",
    "title",
    "original_title",
    "year",
    "date_published",
    "genre",
    "duration",
    "country",
    "language",
    "director",
    "writer",
    "production_company",
    "actors",
    "description","avg_vote",
    "votes",
    "budget",
    "usa_gross_income",
    "worlwide_gross_income",
    "metascore",
    "reviews_from_users",
    "reviews_from_critics"
];


let mode: any;
await fs.stat(TYPES_PATH)
.then((s: Stats) => {
    mode = s.mode;
});

console.log({mode});

const CSV_FILE = await fs.open(CSV_PATH);
// const TYPES_FILE = await fs.open(TYPES_PATH, undefined, mode);

let parsed_csv: Movie[] = []

await CSV_FILE.readFile({encoding: "utf-8"})
    .then((csv_data: string) => {
        parse(
            csv_data, 
            {
                delimiter: ",",
                columns: CSV_HEADERS
            },
            (err, res: Movie[]) => {
                res.shift();
                // console.log({"res[0]": res[0]});
                // TYPES_FILE.appendFile(`\n export type Genre = ${getProperty(res)}; \n`, {
                //     encoding: "utf-8"
                // })
                //     .then((res: void) => console.log("DONE"))
                //     .catch((err: any) => console.error(err))
                //     .finally(() => TYPES_FILE.close());
                console.log(`\nexport type Country = ${getProperty(res)}; \n`);
            }
        );
    })
    .finally(() => CSV_FILE.close());

function getProperty(data: Movie[]): string {
    let property: Array<string> = []

    for (const MOVIE of data) {
        const MOVIE_GENRES = MOVIE.country.split(", ");
        MOVIE_GENRES.forEach((m_g) => {
            if (!property.includes(`"${m_g}"`)) {
                property.push(`"${m_g}"`)
            };
        })
    };

    return property.join(" | ");
};
