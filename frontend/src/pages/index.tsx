/* eslint-disable react/jsx-key */
import React, {JSX} from 'react';

import Image from 'next/image'
import { Inter } from 'next/font/google'

import { Sample } from '@/utils/data';
import { Movie } from '@/utils/types';

const inter = Inter({ subsets: ['latin'] });

const TableHeader = (props: {header_string: string}): JSX.Element => {

    return (
        <th className="border-2 border-sky-500">{props.header_string}</th>
    );
};

const TableRow = (props: {movie: Movie}): JSX.Element => {

    return (
        <tr className="table-row">
            {Object.values(props.movie).map((movie_prop: any) => <td className="border-2 border-sky-500 box-content max-h-12 overflow-hidden text-ellipsis"><p>{movie_prop}</p></td>)}
        </tr>
    );
};

export default function Home() {

    const HEADERS: string[] = Object.keys(Sample[0]);

    return (
        <main className={`flex min-h-screen min-w-fit w-full flex-col items-center justify-between p-24 ${inter.className}`} >
            hello there
            <table className="border-separate table-fixed border-2 border-sky-500 border-spacing-1">
                <thead>
                    <tr className="border-2 border-sky-500 table-row">
                        {
                            HEADERS.map((header: string) => <TableHeader header_string={header} />)
                        }
                    </tr>
                </thead>
                <tbody className="">
                    {
                        Sample.map((movie_item) => <TableRow movie={movie_item}/>)
                    }
                </tbody>
            </table>
        </main>
    );
};

