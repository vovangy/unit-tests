import type { SortBy } from '../types';

export const getNextSortBy = (sortBy: SortBy): SortBy => {
    if (sortBy === 'по умолчанию') {
        return 'по возрастанию цены';
    }

    if (sortBy === 'по возрастанию цены') {
        return 'по убыванию цены';
    }

    return 'по умолчанию';
};
