/* eslint-disable react/jsx-key */
import React, {JSX} from 'react';

import Image from 'next/image'
import { Inter } from 'next/font/google'

import { Sample } from '@/utils/data';
import { Movie } from '@/utils/types';

const inter = Inter({ subsets: ['latin'] });

const TableHeader = (props: {header_string: string}): JSX.Element => {

    return (
        <th>{props.header_string}</th>
    );
};


const TableRow = (props: {movie: Movie}): JSX.Element => {

    return (
        <tr>
            {Object.values(props.movie).map((movie_prop: any) => <td>{movie_prop}</td>)}
        </tr>
    );
};

export default function Home() {

    const HEADERS: string[] = Object.keys(Sample[0]);

    return (
        <main className={`flex min-h-screen flex-col items-center justify-between p-24 ${inter.className}`} >
            hello there
            <table>
                <thead>
                    <tr>
                        {
                            HEADERS.map((header: string) => <TableHeader header_string={header} />)
                        }
                    </tr>
                </thead>
                <tbody>
                    {
                        Sample.map((movie_item) => <TableRow movie={movie_item}/>)
                    }
                </tbody>
            </table>
        </main>
    );
};

