import { expect } from 'chai';
import { checkAccessibility } from '../src/js/accessibility';

describe('Accessibility Tests', () => {
    it('should have no accessibility violations on the overview page', async () => {
        const violations = await checkAccessibility('src/pages/overview.html');
        expect(violations).to.be.empty;
    });

    it('should have no accessibility violations on the processing page', async () => {
        const violations = await checkAccessibility('src/pages/processing.html');
        expect(violations).to.be.empty;
    });

    it('should have no accessibility violations on the preservation page', async () => {
        const violations = await checkAccessibility('src/pages/preservation.html');
        expect(violations).to.be.empty;
    });

    it('should have no accessibility violations on the food safety page', async () => {
        const violations = await checkAccessibility('src/pages/food-safety.html');
        expect(violations).to.be.empty;
    });

    it('should have no accessibility violations on the resources page', async () => {
        const violations = await checkAccessibility('src/pages/resources.html');
        expect(violations).to.be.empty;
    });
});