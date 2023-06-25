import React, {JSX} from 'react';

import Image from 'next/image';
import { Inter } from 'next/font/google';

import { Sample } from '@/utils/data';

const inter = Inter({ subsets: ['latin'] });

const TableHeader = (header_string: string): JSX.Element => {

    return (
        <th>{header_string}</th>
    );
};

export default function Home() {

    const HEADERS: string[] = Object.keys(Sample[0]);
    

    return (
        <main className={`flex min-h-screen flex-col items-center justify-between p-24 ${inter.className}`} >
            <table>
                {
                    HEADERS.map(
                        (header: string) => {
                            return (
                                <React.Fragment key={1}>
                                    <TableHeader header_string={header} />
                                </React.Fragment>
                            );
                        }
                    )
                }
            </table>
        </main>
    );
};

