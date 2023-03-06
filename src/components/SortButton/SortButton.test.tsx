import React from 'react';

import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { SortButton } from './SortButton';

describe('Button render', () => {
    it('should contain sort text', () => {
        const onSortButtonClick = jest.fn();
        const renderedButton = render(
            <SortButton
                currentSort="по умолчанию"
                onSortButtonClick={onSortButtonClick}
            />
        );

        expect(renderedButton.getByRole('button')).toHaveTextContent(
            'Сортировать по умолчанию'
        );

        expect(onSortButtonClick).toHaveBeenCalledTimes(0);
        fireEvent.click(renderedButton.getByRole('button'));
        expect(onSortButtonClick).toHaveBeenCalledTimes(1);

        expect(renderedButton.asFragment()).toMatchSnapshot();
    });
});
